"""Password Cracking Time Simulation Engine"""

import math
import string


class CrackTimeSimulator:
    """Simulate time to crack passwords using different attack methods"""
    
    # Attacker speed profiles (guesses per second)
    ATTACKER_SPEED = {
        "basic": 1e6,      # 1 million guesses/sec
        "gpu": 1e9,        # 1 billion guesses/sec
        "ai": 1e11         # 100 billion guesses/sec (AI-enhanced)
    }
    
    def __init__(self):
        self.charset_sizes = {
            'lowercase': 26,
            'uppercase': 26,
            'digits': 10,
            'special': 32
        }
    
    def calculate_search_space(self, password):
        """Calculate the theoretical search space for a password"""
        # Determine character set size
        charset_size = 0
        
        if any(c.islower() for c in password):
            charset_size += self.charset_sizes['lowercase']
        if any(c.isupper() for c in password):
            charset_size += self.charset_sizes['uppercase']
        if any(c.isdigit() for c in password):
            charset_size += self.charset_sizes['digits']
        if any(c in string.punctuation for c in password):
            charset_size += self.charset_sizes['special']
        
        # Search space = charset_size ^ password_length
        search_space = charset_size ** len(password)
        return search_space
    
    def estimate_crack_time(self, password, attack_type="basic"):
        """Estimate time to crack password"""
        search_space = self.calculate_search_space(password)
        guesses_per_sec = self.ATTACKER_SPEED.get(attack_type, self.ATTACKER_SPEED["basic"])
        
        # Average case: need to try 50% of search space
        average_attempts = search_space / 2
        
        # Time in seconds
        time_seconds = average_attempts / guesses_per_sec
        
        return {
            'search_space': search_space,
            'guesses_per_sec': guesses_per_sec,
            'time_seconds': time_seconds,
            'time_formatted': self.format_time(time_seconds),
            'attack_type': attack_type
        }
    
    def estimate_all_attacks(self, password):
        """Estimate crack time for all attack types"""
        results = {}
        for attack_type in self.ATTACKER_SPEED.keys():
            results[attack_type] = self.estimate_crack_time(password, attack_type)
        return results
    
    def format_time(self, seconds):
        """Format time in human-readable format"""
        if seconds < 1:
            return "Instant"
        elif seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.2f} minutes"
        elif seconds < 86400:
            hours = seconds / 3600
            return f"{hours:.2f} hours"
        elif seconds < 31536000:
            days = seconds / 86400
            return f"{days:.2f} days"
        elif seconds < 31536000000:
            years = seconds / 31536000
            return f"{years:.2f} years"
        else:
            return f"{seconds / 31536000:.2e} years"
    
    def get_risk_level(self, time_seconds):
        """Determine risk level based on crack time"""
        if time_seconds < 3600:  # Less than 1 hour
            return "CRITICAL"
        elif time_seconds < 86400:  # Less than 1 day
            return "HIGH"
        elif time_seconds < 2592000:  # Less than 30 days
            return "MEDIUM"
        else:
            return "LOW"
    
    def calculate_strength_score(self, password):
        """Calculate overall strength score (0-100)"""
        score = 0
        
        # Length contribution (max 25 points)
        length = len(password)
        score += min(length * 2.5, 25)
        
        # Character diversity (max 25 points)
        char_types = sum([
            any(c.islower() for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            any(c in string.punctuation for c in password)
        ])
        score += char_types * 6.25
        
        # Entropy contribution (max 25 points)
        # Simplified entropy estimation
        unique_chars = len(set(password))
        if length > 0:
            diversity_ratio = unique_chars / length
            score += diversity_ratio * 25
        
        # Crack time contribution (max 25 points)
        crack_time = self.estimate_crack_time(password, "ai")
        time_score = min(math.log10(max(crack_time['time_seconds'], 1)) * 2.5, 25)
        score += time_score
        
        return min(int(score), 100)
