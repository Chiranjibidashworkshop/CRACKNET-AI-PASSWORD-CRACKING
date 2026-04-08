# CrackNet - Quick Start Guide

## 🚀 Getting Started in VSCode

### 1. Prerequisites
- Python 3.8+ installed
- VSCode with Python extension
- Terminal access

### 2. Setup Instructions

#### Step 1: Open Project in VSCode
```bash
# Navigate to project directory
cd /path/to/cracknet

# Open in VSCode
code .
```

#### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Configure Environment
```bash
# Copy .env file and edit it
# Add your HIBP API key (optional)
```

#### Step 5: Prepare Data and Train Model
```bash
# Clean data (uses sample dataset if RockYou not available)
python src/clean_data.py

# Train the model
python src/train_model.py
```

#### Step 6: Run the Application
```bash
# Start Flask server
python src/app/app.py
```

The application will be available at `http://localhost:5000`

---

## 📂 File Structure Overview

```
CrackNet/
├── src/
│   ├── app/
│   │   ├── app.py              # Main Flask application
│   │   ├── features/
│   │   │   └── utils.py        # Feature extraction
│   │   ├── templates/
│   │   │   └── index.html      # Frontend HTML
│   │   └── static/
│   │       ├── css/style.css   # Styling
│   │       └── js/main.js      # JavaScript
│   ├── simulator/
│   │   └── crack_time.py       # Time estimation
│   ├── clean_data.py           # Data preprocessing
│   └── train_model.py          # Model training
├── data/
│   ├── raw/                    # Raw datasets
│   └── processed/              # Processed data
├── models/                     # Trained ML models
├── requirements.txt            # Python dependencies
└── .env                        # Environment variables
```

---

## 🔑 Key Features to Explore

### 1. Password Analysis
- Enter any password to get comprehensive analysis
- Get strength classification (Weak/Medium/Strong)
- View security score (0-100)
- See time-to-crack estimates

### 2. Pattern Detection
- Identifies leet speak (@ for a, 3 for e)
- Detects common patterns
- Finds sequential characters
- Recognizes keyboard patterns

### 3. Breach Check
- Uses Have I Been Pwned API
- Shows if password was compromised
- Displays breach count

### 4. Security Scorecard
- Lists strengths of your password
- Highlights weaknesses
- Provides actionable recommendations

---

## 🧪 Testing the Application

### Test Passwords:

**Weak Passwords:**
- `123456` - Very weak, common pattern
- `password` - Dictionary word
- `qwerty` - Keyboard pattern

**Medium Passwords:**
- `Password123` - Has variety but common pattern
- `Welcome2024` - Decent but predictable

**Strong Passwords:**
- `Tr0ub4dor&3` - Good mix with special chars
- `MyP@ssw0rd!2024` - Complex with symbols
- `C0mpl3x!ty#2024` - High entropy

### API Testing with curl:

```bash
# Analyze password
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"password":"TestPassword123!"}'

# Check breach
curl -X POST http://localhost:5000/api/check_breach \
  -H "Content-Type: application/json" \
  -d '{"password":"password123"}'

# Health check
curl http://localhost:5000/api/health
```

---

## 🎯 Development Tips

### Debugging in VSCode

1. **Create launch.json:**
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "src/app/app.py",
                "FLASK_DEBUG": "1"
            },
            "args": ["run"],
            "jinja": true
        }
    ]
}
```

2. **Set Breakpoints:**
   - Click left of line numbers
   - Press F5 to start debugging

### Hot Reload
Flask has auto-reload enabled in debug mode. Just save your files and Flask will restart automatically.

---

## 📊 Model Retraining

If you want to retrain with your own dataset:

```bash
# 1. Place your password file in data/raw/rockyou.txt
# 2. Clean and process
python src/clean_data.py

# 3. Retrain model
python src/train_model.py
```

The model will show:
- Accuracy score
- Classification report
- Feature importance
- Confusion matrix

---

## 🔧 Common Issues & Solutions

### Issue: ModuleNotFoundError
**Solution:** Make sure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: Model not loading
**Solution:** Ensure you've run the training script
```bash
python src/train_model.py
```

### Issue: HIBP API rate limit
**Solution:** Get an API key from https://haveibeenpwned.com/API/Key

### Issue: Port 5000 already in use
**Solution:** Change port in .env file or stop the conflicting service

---

## 📚 Further Customization

### Adding New Features
1. Edit `src/app/features/utils.py` to add new feature extraction
2. Update `train_model.py` to include new features
3. Retrain the model

### Changing Attack Speeds
Edit `ATTACKER_SPEED` in `src/simulator/crack_time.py`:
```python
ATTACKER_SPEED = {
    "basic": 1e6,
    "gpu": 1e9,
    "ai": 1e11
}
```

### Customizing UI
- Colors: Edit CSS variables in `src/app/static/css/style.css`
- Layout: Modify `src/app/templates/index.html`
- Behavior: Update `src/app/static/js/main.js`

---

## 🎓 Educational Use

This project demonstrates:
- Machine Learning for cybersecurity
- Random Forest classification
- Feature engineering
- Flask web development
- REST API design
- Frontend integration
- Data preprocessing
- Password security concepts

---

## ⚠️ Important Notes

1. **Never** test real passwords you use
2. **Never** store or log user passwords
3. Use only for educational purposes
4. Follow ethical hacking guidelines
5. Respect privacy and security

---

## 📞 Support

For issues or questions:
1. Check the main README.md
2. Review code comments
3. Test with sample passwords first
4. Check browser console for errors
5. Review Flask logs in terminal

---

## 🎉 Success Checklist

- [ ] Virtual environment created and activated
- [ ] Dependencies installed
- [ ] Data cleaned and processed
- [ ] Model trained successfully
- [ ] Flask server running
- [ ] Web interface accessible
- [ ] API endpoints working
- [ ] Password analysis functional
- [ ] Breach check operational
- [ ] All features tested

---

**Happy Coding! 🚀**
