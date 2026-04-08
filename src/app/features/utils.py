"""Feature Extraction Utilities for Password Analysis"""

import re
import math
from collections import Counter
import string


class PasswordFeatureExtractor:
    """Extract features from passwords for ML analysis"""
    
    def __init__(self):
        self.leet_speak_map = {
            '0': 'o', '1': 'i', '3': 'e', '4': 'a', 
            '5': 's', '7': 't', '8': 'b', '@': 'a', 
            '$': 's', '!': 'i'
        }
        
        self.common_patterns = [
            r'123', r'abc', r'qwerty', r'password', 
            r'admin', r'letmein', r'welcome'
        ]
    
    def extract_all_features(self, password):
        """Extract all features from a password"""
        features = {
            'length': len(password),
            'entropy': self.calculate_entropy(password),
            'has_uppercase': int(any(c.isupper() for c in password)),
            'has_lowercase': int(any(c.islower() for c in password)),
            'has_digit': int(any(c.isdigit() for c in password)),
            'has_special': int(any(c in string.punctuation for c in password)),
            'uppercase_count': sum(1 for c in password if c.isupper()),
            'lowercase_count': sum(1 for c in password if c.islower()),
            'digit_count': sum(1 for c in password if c.isdigit()),
            'special_count': sum(1 for c in password if c in string.punctuation),
            'char_diversity': len(set(password)) / len(password) if len(password) > 0 else 0,
            'has_leet_speak': int(self.detect_leet_speak(password)),
            'has_common_pattern': int(self.detect_common_patterns(password)),
            'sequential_chars': self.count_sequential_chars(password),
            'repeated_chars': self.count_repeated_chars(password),
            'keyboard_patterns': int(self.detect_keyboard_patterns(password))
        }
        return features
    
    def calculate_entropy(self, password):
        """Calculate Shannon entropy of password"""
        if not password:
            return 0
        
        # Count character frequencies
        freq = Counter(password)
        length = len(password)
        
        # Calculate entropy
        entropy = 0
        for count in freq.values():
            probability = count / length
            entropy -= probability * math.log2(probability)
        
        return round(entropy, 4)
    
    def detect_leet_speak(self, password):
        """Detect leet speak substitutions"""
        for leet_char in self.leet_speak_map.keys():
            if leet_char in password:
                return True
        return False
    
    def detect_common_patterns(self, password):
        """Detect common password patterns"""
        password_lower = password.lower()
        for pattern in self.common_patterns:
            if re.search(pattern, password_lower):
                return True
        return False
    
    def count_sequential_chars(self, password):
        """Count sequential characters (e.g., 'abc', '123')"""
        sequential_count = 0
        for i in range(len(password) - 2):
            if password[i:i+3].isalpha():
                if ord(password[i+1]) == ord(password[i]) + 1 and \
                   ord(password[i+2]) == ord(password[i+1]) + 1:
                    sequential_count += 1
            elif password[i:i+3].isdigit():
                if int(password[i+1]) == int(password[i]) + 1 and \
                   int(password[i+2]) == int(password[i+1]) + 1:
                    sequential_count += 1
        return sequential_count
    
    def count_repeated_chars(self, password):
        """Count repeated consecutive characters"""
        if not password:
            return 0
        
        repeated = 0
        for i in range(len(password) - 1):
            if password[i] == password[i+1]:
                repeated += 1
        return repeated
    
    def detect_keyboard_patterns(self, password):
        """Detect keyboard patterns (qwerty, asdf, etc.)"""
        keyboard_patterns = [
            'qwerty', 'asdfgh', 'zxcvbn',
            'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        ]
        password_lower = password.lower()
        for pattern in keyboard_patterns:
            if pattern in password_lower or pattern[::-1] in password_lower:
                return True
        return False
    
    def analyze_patterns(self, password):
        """Detailed pattern analysis for feedback"""
        patterns = []
        
        if self.detect_leet_speak(password):
            patterns.append("Leet speak detected (e.g., @ for a, 3 for e)")
        
        if self.detect_common_patterns(password):
            patterns.append("Common password pattern detected")
        
        if self.count_sequential_chars(password) > 0:
            patterns.append("Sequential characters found (e.g., abc, 123)")
        
        if self.count_repeated_chars(password) > 2:
            patterns.append("Multiple repeated characters")
        
        if self.detect_keyboard_patterns(password):
            patterns.append("Keyboard pattern detected (e.g., qwerty)")
        
        if len(password) < 8:
            patterns.append("Password too short (minimum 8 characters recommended)")
        
        char_types = sum([
            any(c.isupper() for c in password),
            any(c.islower() for c in password),
            any(c.isdigit() for c in password),
            any(c in string.punctuation for c in password)
        ])
        
        if char_types < 3:
            patterns.append(f"Limited character variety (using only {char_types}/4 types)")
        
        return patterns
