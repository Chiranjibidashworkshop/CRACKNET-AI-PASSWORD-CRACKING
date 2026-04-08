"""Flask Backend for CrackNet - AI Password Analysis System"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import os
import sys
from pathlib import Path
import requests
import hashlib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from features.utils import PasswordFeatureExtractor
from simulator.crack_time import CrackTimeSimulator

app = Flask(__name__)
CORS(app)

# Configuration
BASE_DIR = Path(__file__).parent.parent.parent
MODEL_PATH = os.getenv('MODEL_PATH', str(BASE_DIR / 'models' / 'password_model.pkl'))
ENCODER_PATH = os.getenv('ENCODER_PATH', str(BASE_DIR / 'models' / 'label_encoder.pkl'))
HIBP_API_KEY = os.getenv('HIBP_API_KEY', '')

# Initialize components
feature_extractor = PasswordFeatureExtractor()
crack_simulator = CrackTimeSimulator()

# Load ML model
try:
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    MODEL_LOADED = True
    print("✅ ML Model loaded successfully!")
except Exception as e:
    print(f"⚠️ Warning: Could not load ML model: {e}")
    print("Model prediction will be based on heuristics.")
    MODEL_LOADED = False


@app.route('/')
def index():
    """Render main dashboard"""
    return render_template('index.html')


@app.route('/api/analyze', methods=['POST'])
def analyze_password():
    """Comprehensive password analysis endpoint"""
    try:
        data = request.get_json()
        password = data.get('password', '')
        
        if not password:
            return jsonify({'error': 'Password is required'}), 400
        
        # Extract features
        features = feature_extractor.extract_all_features(password)
        
        # Get ML prediction
        if MODEL_LOADED:
            feature_vector = [
                features['length'], features['entropy'],
                features['has_uppercase'], features['has_lowercase'],
                features['has_digit'], features['has_special'],
                features['uppercase_count'], features['lowercase_count'],
                features['digit_count'], features['special_count'],
                features['char_diversity'], features['has_leet_speak'],
                features['has_common_pattern'], features['sequential_chars'],
                features['repeated_chars'], features['keyboard_patterns']
            ]
            
            prediction = model.predict([feature_vector])[0]
            strength = label_encoder.inverse_transform([prediction])[0]
            confidence = max(model.predict_proba([feature_vector])[0]) * 100
        else:
            # Fallback heuristic classification
            strength = heuristic_classification(features)
            confidence = 75.0
        
        # Pattern analysis
        patterns = feature_extractor.analyze_patterns(password)
        
        # Crack time estimation
        crack_times = crack_simulator.estimate_all_attacks(password)
        
        # Calculate strength score
        strength_score = crack_simulator.calculate_strength_score(password)
        
        # Risk level
        risk_level = crack_simulator.get_risk_level(
            crack_times['ai']['time_seconds']
        )
        
        # Generate security scorecard
        scorecard = generate_security_scorecard(
            features, patterns, strength, crack_times
        )
        
        # Response
        response = {
            'success': True,
            'password_length': len(password),
            'strength': strength,
            'strength_score': strength_score,
            'confidence': round(confidence, 2),
            'risk_level': risk_level,
            'features': features,
            'patterns_detected': patterns,
            'crack_times': {
                'basic': crack_times['basic']['time_formatted'],
                'gpu': crack_times['gpu']['time_formatted'],
                'ai': crack_times['ai']['time_formatted']
            },
            'crack_times_raw': {
                'basic': crack_times['basic']['time_seconds'],
                'gpu': crack_times['gpu']['time_seconds'],
                'ai': crack_times['ai']['time_seconds']
            },
            'scorecard': scorecard
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/check_breach', methods=['POST'])
def check_breach():
    """Check if password has been exposed in data breaches (HIBP)"""
    try:
        data = request.get_json()
        password = data.get('password', '')
        
        if not password:
            return jsonify({'error': 'Password is required'}), 400
        
        # Hash password with SHA-1
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        hash_prefix = sha1_hash[:5]
        hash_suffix = sha1_hash[5:]
        
        # Query HIBP API (k-anonymity model)
        url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
        headers = {}
        
        if HIBP_API_KEY:
            headers['hibp-api-key'] = HIBP_API_KEY
        
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            # Parse response
            hashes = response.text.split('\r\n')
            for hash_entry in hashes:
                if ':' in hash_entry:
                    hash_part, count = hash_entry.split(':')
                    if hash_part == hash_suffix:
                        return jsonify({
                            'success': True,
                            'breached': True,
                            'breach_count': int(count),
                            'message': f'⚠️ This password has been seen {count} times in data breaches!'
                        }), 200
            
            # Not found in breaches
            return jsonify({
                'success': True,
                'breached': False,
                'breach_count': 0,
                'message': '✅ This password has not been found in known data breaches.'
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Unable to check breach status'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Breach check failed: {str(e)}'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': MODEL_LOADED,
        'hibp_configured': bool(HIBP_API_KEY)
    }), 200


def heuristic_classification(features):
    """Fallback heuristic classification when model is not available"""
    score = 0
    
    if features['length'] >= 12:
        score += 3
    elif features['length'] >= 8:
        score += 2
    
    char_types = sum([
        features['has_uppercase'],
        features['has_lowercase'],
        features['has_digit'],
        features['has_special']
    ])
    score += char_types
    
    if features['entropy'] >= 4.0:
        score += 2
    elif features['entropy'] >= 3.0:
        score += 1
    
    if features['has_common_pattern']:
        score -= 2
    if features['has_leet_speak']:
        score -= 1
    
    if score >= 7:
        return "Strong"
    elif score >= 4:
        return "Medium"
    else:
        return "Weak"


def generate_security_scorecard(features, patterns, strength, crack_times):
    """Generate educational security scorecard"""
    scorecard = {
        'overall_assessment': '',
        'strengths': [],
        'weaknesses': [],
        'recommendations': []
    }
    
    # Overall assessment
    if strength == "Strong":
        scorecard['overall_assessment'] = "Your password demonstrates good security practices."
    elif strength == "Medium":
        scorecard['overall_assessment'] = "Your password has moderate security but could be improved."
    else:
        scorecard['overall_assessment'] = "Your password is vulnerable to attacks. Immediate improvement needed."
    
    # Strengths
    if features['length'] >= 12:
        scorecard['strengths'].append(f"Good length ({features['length']} characters)")
    
    if features['entropy'] >= 4.0:
        scorecard['strengths'].append(f"High entropy ({features['entropy']:.2f})")
    
    char_types = sum([
        features['has_uppercase'],
        features['has_lowercase'],
        features['has_digit'],
        features['has_special']
    ])
    if char_types >= 3:
        scorecard['strengths'].append(f"Good character variety ({char_types}/4 types)")
    
    if features['char_diversity'] >= 0.7:
        scorecard['strengths'].append("High character diversity")
    
    # Weaknesses
    if features['length'] < 8:
        scorecard['weaknesses'].append(f"Too short ({features['length']} characters)")
    
    if char_types < 3:
        scorecard['weaknesses'].append(f"Limited character types ({char_types}/4)")
    
    if features['has_common_pattern']:
        scorecard['weaknesses'].append("Contains common password patterns")
    
    if features['has_leet_speak']:
        scorecard['weaknesses'].append("Leet speak is easily detected by AI")
    
    if features['sequential_chars'] > 0:
        scorecard['weaknesses'].append("Contains sequential characters")
    
    if features['keyboard_patterns']:
        scorecard['weaknesses'].append("Contains keyboard patterns")
    
    # Recommendations
    if features['length'] < 12:
        scorecard['recommendations'].append("Increase length to at least 12 characters")
    
    if char_types < 4:
        scorecard['recommendations'].append("Use all character types (upper, lower, digits, special)")
    
    if features['has_common_pattern']:
        scorecard['recommendations'].append("Avoid common words and patterns")
    
    if crack_times['ai']['time_seconds'] < 86400:
        scorecard['recommendations'].append("Current password can be cracked quickly by AI - consider using a passphrase")
    
    if not scorecard['strengths']:
        scorecard['strengths'].append("None identified - password needs significant improvement")
    
    if not scorecard['weaknesses']:
        scorecard['weaknesses'].append("None identified - excellent password!")
    
    if not scorecard['recommendations']:
        scorecard['recommendations'].append("Maintain current password practices")
    
    return scorecard


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    app.run(host=host, port=port, debug=True)
