"""Data Cleaning and Processing Script"""

import pandas as pd
import numpy as np
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent))
from app.features.utils import PasswordFeatureExtractor


def clean_dataset(input_file, output_file, sample_size=100000):
    """Clean and process password dataset"""
    
    print(f"Reading dataset from {input_file}...")
    
    passwords = []
    try:
        with open(input_file, 'r', encoding='latin-1', errors='ignore') as f:
            for line in f:
                password = line.strip()
                if password and len(password) >= 4 and len(password) <= 50:
                    passwords.append(password)
                if len(passwords) >= sample_size:
                    break
    except FileNotFoundError:
        print(f"Error: File {input_file} not found!")
        print("Creating sample dataset instead...")
        passwords = create_sample_dataset()
    
    print(f"Loaded {len(passwords)} passwords")
    
    # Extract features
    print("Extracting features...")
    extractor = PasswordFeatureExtractor()
    data = []
    
    for i, password in enumerate(passwords):
        if i % 10000 == 0:
            print(f"Processed {i}/{len(passwords)} passwords...")
        
        features = extractor.extract_all_features(password)
        features['password'] = password
        features['label'] = label_password_strength(features)
        data.append(features)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save processed data
    print(f"Saving processed data to {output_file}...")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    
    print(f"✅ Data cleaning complete! Saved {len(df)} records.")
    print(f"\nLabel distribution:")
    print(df['label'].value_counts())
    
    return df


def label_password_strength(features):
    """Label password strength based on features"""
    score = 0
    
    # Length scoring
    if features['length'] >= 12:
        score += 3
    elif features['length'] >= 8:
        score += 2
    else:
        score += 1
    
    # Character diversity
    char_types = sum([
        features['has_uppercase'],
        features['has_lowercase'],
        features['has_digit'],
        features['has_special']
    ])
    score += char_types
    
    # Entropy
    if features['entropy'] >= 4.0:
        score += 2
    elif features['entropy'] >= 3.0:
        score += 1
    
    # Penalties
    if features['has_common_pattern']:
        score -= 2
    if features['has_leet_speak']:
        score -= 1
    if features['sequential_chars'] > 0:
        score -= 1
    if features['repeated_chars'] > 2:
        score -= 1
    
    # Final classification
    if score >= 7:
        return "Strong"
    elif score >= 4:
        return "Medium"
    else:
        return "Weak"


def create_sample_dataset():
    """Create a sample dataset for testing"""
    print("Creating sample dataset...")
    
    weak_passwords = [
        "123456", "password", "12345678", "qwerty", "abc123",
        "monkey", "letmein", "trustno1", "dragon", "baseball",
        "iloveyou", "master", "sunshine", "ashley", "bailey"
    ] * 100
    
    medium_passwords = [
        "Password1", "Welcome123", "Hello2024", "Admin@123",
        "User1234", "Test@123", "MyPass123", "Secure1",
        "Access2024", "Login@99", "Pass1word", "System123"
    ] * 100
    
    strong_passwords = [
        "Tr0ub4dor&3", "correcthorsebatterystaple", "MyP@ssw0rd!2024",
        "X9#mK2$pL5@vN8", "Secure_P@ss_2024!", "C0mpl3x!ty#2024",
        "R@nd0m$tr0ng#Pass", "Un1qu3_S3cur3!P@ss", "Str0ng&S@f3_2024",
        "MyV3ry$3cur3P@ss!", "C0mpl3xP@ssw0rd#123"
    ] * 100
    
    return weak_passwords + medium_passwords + strong_passwords


if __name__ == "__main__":
    input_file = "data/raw/rockyou.txt"
    output_file = "data/processed/cleaned_passwords.csv"
    
    clean_dataset(input_file, output_file, sample_size=100000)
