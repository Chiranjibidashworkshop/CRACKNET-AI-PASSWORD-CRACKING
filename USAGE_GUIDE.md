# 🎯 CrackNet - Complete Usage Guide

## 🚀 Running the Application

### Current Status
✅ **Application is RUNNING on port 5000**

### Access the Dashboard
Open your browser and visit:
```
http://localhost:5000
```

---

## 📖 Step-by-Step Usage

### 1. Analyze a Password

1. **Navigate to** http://localhost:5000
2. **Enter a password** in the input field
3. **Click "Analyze Password"** button
4. **View Results:**
   - Strength classification (Weak/Medium/Strong)
   - Security score (0-100)
   - Risk level (Critical/High/Medium/Low)
   - Time-to-crack estimates for different attacks
   - Detected patterns and weaknesses
   - Comprehensive security scorecard

### 2. Check Breach Status

1. **Enter a password** in the input field
2. **Click "Check Breach Status"** button
3. **See if the password was compromised:**
   - If breached: Shows number of times seen in data breaches
   - If safe: Confirms password not found in known breaches

---

## 🧪 Test Examples

### Test These Passwords:

#### Weak Passwords
```
123456
password
qwerty
letmein
admin
```

**Expected Results:**
- Strength: Weak
- Score: < 40
- Risk: Critical/High
- Quick crack time
- Multiple pattern warnings

#### Medium Passwords
```
Password123
Welcome2024
Admin@123
MyPass2024
```

**Expected Results:**
- Strength: Medium
- Score: 40-70
- Risk: Medium
- Moderate crack time
- Some pattern warnings

#### Strong Passwords
```
Tr0ub4dor&3
MyP@ssw0rd!2024
C0mpl3x!ty#2024
R@nd0m$tr0ng#Pass
```

**Expected Results:**
- Strength: Strong
- Score: 70-100
- Risk: Low
- Very long crack time
- Few or no warnings

---

## 🔌 API Usage

### Health Check
```bash
curl http://localhost:5000/api/health
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "hibp_configured": true
}
```

### Analyze Password
```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"password":"YourPasswordHere"}'
```

**Response Example:**
```json
{
  "success": true,
  "strength": "Medium",
  "strength_score": 65,
  "risk_level": "MEDIUM",
  "crack_times": {
    "basic": "10.5 years",
    "gpu": "3.8 days",
    "ai": "5.2 hours"
  },
  "patterns_detected": [
    "Common password pattern detected"
  ],
  "scorecard": {
    "overall_assessment": "Your password has moderate security...",
    "strengths": [...],
    "weaknesses": [...],
    "recommendations": [...]
  }
}
```

### Check Breach
```bash
curl -X POST http://localhost:5000/api/check_breach \
  -H "Content-Type: application/json" \
  -d '{"password":"password123"}'
```

**Response Example:**
```json
{
  "success": true,
  "breached": true,
  "breach_count": 2254650,
  "message": "⚠️ This password has been seen 2254650 times in data breaches!"
}
```

---

## 🎓 Understanding the Results

### Strength Classification

**Weak:**
- Short length (< 8 characters)
- Limited character types
- Common patterns
- Low entropy
- Easily crackable

**Medium:**
- Decent length (8-12 characters)
- Multiple character types
- Some patterns detected
- Moderate entropy
- Moderately secure

**Strong:**
- Good length (12+ characters)
- All character types used
- No common patterns
- High entropy
- Very secure

### Security Score (0-100)

- **0-40:** Critical - Needs immediate improvement
- **41-70:** Moderate - Can be improved
- **71-100:** Excellent - Strong security

### Risk Levels

- **CRITICAL:** Can be cracked in < 1 hour
- **HIGH:** Can be cracked in < 1 day
- **MEDIUM:** Can be cracked in < 30 days
- **LOW:** Takes 30+ days to crack

### Time-to-Crack Attacks

1. **Basic Attack (1M guesses/sec)**
   - Standard CPU-based brute force
   - Slowest but most common

2. **GPU Attack (1B guesses/sec)**
   - Graphics card acceleration
   - 1000x faster than basic

3. **AI-Enhanced Attack (100B guesses/sec)**
   - Machine learning patterns
   - 100,000x faster than basic
   - Most realistic modern threat

---

## 🔍 Pattern Detection

### Detected Patterns:

1. **Leet Speak**
   - @ for a, 3 for e, $ for s
   - Example: "P@ssw0rd"
   - Why it matters: Easily detected by AI

2. **Common Patterns**
   - password, 123456, qwerty
   - Dictionary words
   - Common substitutions

3. **Sequential Characters**
   - abc, 123, xyz
   - Consecutive letters or numbers

4. **Keyboard Patterns**
   - qwerty, asdfgh, zxcvbn
   - Keys next to each other

5. **Repeated Characters**
   - aaa, 111, !!!
   - Same character multiple times

---

## 📊 Security Scorecard

### Strengths
Shows what's good about your password:
- Good length
- High entropy
- Character variety
- No common patterns

### Weaknesses
Highlights vulnerabilities:
- Too short
- Limited character types
- Common patterns
- Predictable structure

### Recommendations
Actionable advice:
- Increase length
- Add special characters
- Avoid dictionary words
- Use passphrases

---

## 💡 Best Practices

### Creating Strong Passwords

1. **Length > Complexity**
   - Use 12+ characters
   - Longer is better than complex

2. **Use Passphrases**
   - Example: "correct-horse-battery-staple"
   - Easy to remember, hard to crack

3. **Avoid Personal Information**
   - No names, birthdays, addresses
   - Not in dictionary

4. **Use All Character Types**
   - Uppercase (A-Z)
   - Lowercase (a-z)
   - Numbers (0-9)
   - Special (!@#$%^&*)

5. **Unique for Each Account**
   - Never reuse passwords
   - Use password manager

6. **Enable 2FA**
   - Two-factor authentication
   - Additional security layer

---

## 🛠️ For Developers

### Running in Development

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Run Flask app
python src/app/app.py

# Or using Flask CLI
export FLASK_APP=src/app/app.py
flask run
```

### Retraining the Model

```bash
# Clean data
python src/clean_data.py

# Train model
python src/train_model.py
```

### Viewing Logs

```bash
# Application logs
tail -f /var/log/supervisor/cracknet.out.log

# Error logs
tail -f /var/log/supervisor/cracknet.err.log
```

### Stopping/Starting Service

```bash
# Stop
sudo supervisorctl stop cracknet

# Start
sudo supervisorctl start cracknet

# Restart
sudo supervisorctl restart cracknet

# Status
sudo supervisorctl status cracknet
```

---

## 🎨 Customization

### Changing Attack Speeds

Edit `/app/src/simulator/crack_time.py`:

```python
ATTACKER_SPEED = {
    "basic": 1e6,      # 1 million/sec
    "gpu": 1e9,        # 1 billion/sec
    "ai": 1e11         # 100 billion/sec
}
```

### Modifying UI Colors

Edit `/app/src/app/static/css/style.css`:

```css
:root {
    --primary-color: #667eea;
    --success-color: #10b981;
    --danger-color: #ef4444;
    /* ... more colors ... */
}
```

### Adding New Features

1. **Add to feature extraction** (`src/app/features/utils.py`)
2. **Update training script** (`src/train_model.py`)
3. **Retrain model**
4. **Update UI** if needed

---

## 🐛 Troubleshooting

### Server Not Running

```bash
# Check status
sudo supervisorctl status cracknet

# View logs
tail -f /var/log/supervisor/cracknet.err.log

# Restart
sudo supervisorctl restart cracknet
```

### Model Not Loading

```bash
# Verify model files exist
ls -lh /app/models/

# Retrain if missing
python src/train_model.py
```

### Port Already in Use

Change port in `.env`:
```env
PORT=5001
```

### HIBP Rate Limit

Get API key from:
https://haveibeenpwned.com/API/Key

Add to `.env`:
```env
HIBP_API_KEY=your_key_here
```

---

## 📚 Additional Resources

- **Main README:** `/app/README.md`
- **Quick Start:** `/app/QUICKSTART.md`
- **Project Summary:** `/app/PROJECT_SUMMARY.md`
- **Code Documentation:** Inline comments in source files

---

## ⚠️ Important Reminders

1. **Never test real passwords you use**
2. **This is for educational purposes only**
3. **No passwords are stored or logged**
4. **Use responsibly and ethically**
5. **Follow local laws and regulations**

---

## 🎉 Enjoy Using CrackNet!

For questions or issues, refer to the documentation files or check the code comments.

**Happy Password Analyzing! 🔐**

---

*CrackNet - AI-Based Password Cracking System*
*Built for Cybersecurity Education*
*Version 1.0.0*
