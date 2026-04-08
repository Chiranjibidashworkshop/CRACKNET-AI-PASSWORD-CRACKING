# 🔐 CrackNet - AI-Based Password Cracking System

<div align="center">

![CrackNet Logo](https://img.shields.io/badge/CrackNet-AI%20Security-blueviolet?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask)
![ML](https://img.shields.io/badge/ML-Random%20Forest-orange?style=for-the-badge)

An intelligent password strength analyzer that uses Machine Learning to evaluate password security against modern AI-driven attacks.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [API](#api) • [Documentation](#documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [Testing](#testing)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**CrackNet** is an advanced password security analysis system that goes beyond traditional rule-based password meters. It leverages **Machine Learning** and **AI** to:

- Classify passwords into Weak, Medium, or Strong categories
- Estimate time-to-crack using different attack vectors
- Detect human-predictable patterns that simple checkers miss
- Check if passwords have been exposed in data breaches (HIBP integration)
- Provide educational feedback with a detailed Security Scorecard

Unlike conventional password checkers, CrackNet understands how modern AI-driven attacks work and evaluates passwords accordingly.

---

## ✨ Features

### 🤖 AI-Powered Analysis
- **Random Forest Classifier** trained on real-world leaked password datasets
- 16+ feature extraction metrics (entropy, character diversity, patterns, etc.)
- Sophisticated pattern detection (leet speak, sequential chars, keyboard patterns)

### ⏱️ Cracking Time Simulation
- **Three attack scenarios:**
  - Basic Attack (1M guesses/sec)
  - GPU Attack (1B guesses/sec)
  - AI-Enhanced Attack (100B guesses/sec)
- Real-world time estimates from seconds to centuries

### 🔍 Pattern Detection
- Leet speak detection (`@` for `a`, `3` for `e`, etc.)
- Common password patterns (`password`, `123456`, `qwerty`)
- Sequential characters (`abc`, `123`)
- Keyboard patterns (`qwerty`, `asdfgh`)
- Repeated characters

### 🚨 Breach Detection
- Integration with **Have I Been Pwned (HIBP)** API
- Uses k-anonymity model (only partial hash sent)
- Real-time breach count data

### 📊 Interactive Dashboard
- Modern, responsive UI with dark theme
- Real-time analysis and visualization
- Security scorecard with strengths, weaknesses, and recommendations
- Risk meter and progress indicators

---

## 🛠️ Technology Stack

### Frontend Architecture
- **Framework:** Flask (Python Web Framework)
- **Styling:** Vanilla CSS with custom design system
- **Interactivity:** JavaScript (AJAX/Fetch API)

### Backend Engine
- **Framework:** Flask Server
- **Feature Extraction:** Custom utilities (utils.py)
- **API Integration:** HIBP, REST endpoints

### ML Intelligence
- **Model:** Random Forest Classifier (scikit-learn)
- **Features:** Entropy analysis, pattern detection, character distribution
- **Dataset:** RockYou.txt (100,000+ passwords)

### External APIs
- **HIBP (Have I Been Pwned):** Breach detection

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/cracknet.git
cd cracknet
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
```bash
# Copy the example .env file
cp .env.example .env

# Edit .env and add your HIBP API key (optional but recommended)
# Get your key from: https://haveibeenpwned.com/API/Key
```

### Step 5: Prepare Dataset and Train Model

#### Option A: Use Sample Dataset (Quick Start)
```bash
# Generate sample dataset and train model
python src/clean_data.py
python src/train_model.py
```

#### Option B: Use RockYou Dataset (Recommended for Production)
```bash
# Download RockYou dataset
# Place rockyou.txt in data/raw/ directory

# Clean and process data
python src/clean_data.py

# Train the model
python src/train_model.py
```

### Step 6: Run the Application
```bash
# Start Flask server
python src/app/app.py

# Or using Flask CLI
export FLASK_APP=src/app/app.py
flask run
```

The application will be available at `http://localhost:5000`

---

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Flask Configuration
FLASK_APP=src/app/app.py
FLASK_ENV=development
FLASK_DEBUG=1

# Server Configuration
HOST=0.0.0.0
PORT=5000

# HIBP API
HIBP_API_KEY=your_api_key_here

# Model Paths
MODEL_PATH=models/password_model.pkl
ENCODER_PATH=models/label_encoder.pkl

# Dataset Paths
DATASET_PATH=data/raw/rockyou.txt
PROCESSED_DATA_PATH=data/processed/cleaned_passwords.csv
```

### Getting HIBP API Key

1. Visit [Have I Been Pwned API](https://haveibeenpwned.com/API/Key)
2. Purchase an API key (supports the service)
3. Add the key to your `.env` file

> **Note:** The HIBP integration will work without an API key but may have rate limits.

---

## 🚀 Usage

### Web Interface

1. **Open your browser** and navigate to `http://localhost:5000`
2. **Enter a password** in the input field
3. **Click "Analyze Password"** to get comprehensive analysis
4. **Click "Check Breach Status"** to verify if password is compromised
5. **Review the results:**
   - Strength classification
   - Security score (0-100)
   - Risk level
   - Time-to-crack estimates
   - Pattern detection
   - Security scorecard with recommendations

### Example Passwords to Test

**Weak Passwords:**
- `123456`
- `password`
- `qwerty`

**Medium Passwords:**
- `Password123`
- `Welcome2024`
- `Admin@123`

**Strong Passwords:**
- `Tr0ub4dor&3`
- `MyP@ssw0rd!2024`
- `C0mpl3x!ty#2024`

---

## 📡 API Documentation

### Health Check
```http
GET /api/health
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
```http
POST /api/analyze
Content-Type: application/json

{
  "password": "YourPasswordHere"
}
```

**Response:**
```json
{
  "success": true,
  "password_length": 15,
  "strength": "Strong",
  "strength_score": 85,
  "confidence": 92.5,
  "risk_level": "LOW",
  "features": {
    "length": 15,
    "entropy": 4.2,
    "has_uppercase": 1,
    "has_lowercase": 1,
    "has_digit": 1,
    "has_special": 1,
    ...
  },
  "patterns_detected": [],
  "crack_times": {
    "basic": "1.2 years",
    "gpu": "10.5 hours",
    "ai": "3.8 minutes"
  },
  "scorecard": {
    "overall_assessment": "Your password demonstrates good security practices.",
    "strengths": [...],
    "weaknesses": [...],
    "recommendations": [...]
  }
}
```

### Check Breach Status
```http
POST /api/check_breach
Content-Type: application/json

{
  "password": "YourPasswordHere"
}
```

**Response:**
```json
{
  "success": true,
  "breached": false,
  "breach_count": 0,
  "message": "✅ This password has not been found in known data breaches."
}
```

---

## 📁 Project Structure

```
cracknet/
├── data/
│   ├── raw/
│   │   └── rockyou.txt           # Raw password dataset
│   └── processed/
│       └── cleaned_passwords.csv  # Processed dataset with features
│
├── models/
│   ├── password_model.pkl         # Trained Random Forest model
│   └── label_encoder.pkl          # Label encoder for classifications
│
├── src/
│   ├── app/
│   │   ├── features/
│   │   │   └── utils.py          # Feature extraction utilities
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── style.css     # Frontend styling
│   │   │   └── js/
│   │   │       └── main.js       # Frontend JavaScript
│   │   ├── templates/
│   │   │   └── index.html        # Main dashboard template
│   │   └── app.py                # Flask application
│   │
│   ├── simulator/
│   │   └── crack_time.py         # Cracking time simulation
│   │
│   ├── clean_data.py             # Data cleaning script
│   └── train_model.py            # Model training script
│
├── .env                          # Environment variables
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🎓 Model Training

### Feature Engineering

The system extracts 16 features from each password:

1. **Length** - Total character count
2. **Entropy** - Shannon entropy measure
3. **Has Uppercase** - Presence of uppercase letters
4. **Has Lowercase** - Presence of lowercase letters
5. **Has Digit** - Presence of numbers
6. **Has Special** - Presence of special characters
7. **Uppercase Count** - Number of uppercase letters
8. **Lowercase Count** - Number of lowercase letters
9. **Digit Count** - Number of digits
10. **Special Count** - Number of special characters
11. **Character Diversity** - Ratio of unique characters
12. **Has Leet Speak** - Detection of leet substitutions
13. **Has Common Pattern** - Common password patterns
14. **Sequential Chars** - Sequential character sequences
15. **Repeated Chars** - Repeated consecutive characters
16. **Keyboard Patterns** - Keyboard layout patterns

### Training Process

```bash
# Step 1: Clean and process raw data
python src/clean_data.py

# Step 2: Train Random Forest model
python src/train_model.py
```

### Model Performance

After training, you should see output similar to:

```
✅ Model Accuracy: 94.23%

Classification Report:
              precision    recall  f1-score   support
      
    Medium       0.92      0.91      0.91      4000
    Strong       0.96      0.97      0.97      6000
      Weak       0.95      0.94      0.95     10000

Feature Importance:
              feature  importance
0              length    0.245123
1             entropy    0.189456
10     char_diversity    0.156789
...
```

---

## 🧪 Testing

### Manual Testing

Use the web interface to test various password types and verify:
- Classification accuracy
- Time-to-crack estimates
- Pattern detection
- Breach checking

### API Testing with curl

```bash
# Test analyze endpoint
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"password":"TestPassword123!"}'

# Test breach check
curl -X POST http://localhost:5000/api/check_breach \
  -H "Content-Type: application/json" \
  -d '{"password":"password123"}'
```

---

## 📸 Screenshots

### Main Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### Analysis Results
![Results](docs/screenshots/results.png)

### Security Scorecard
![Scorecard](docs/screenshots/scorecard.png)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

**CrackNet is for educational and research purposes only.**

- Never use this tool to test passwords on live systems without proper authorization
- Never store or log user passwords
- This tool demonstrates password vulnerabilities - use responsibly
- Always follow ethical hacking guidelines and laws

---

## 👥 Authors

**CrackNet Team**
- Educational Project for Cybersecurity Awareness
- SS University

---

## 🙏 Acknowledgments

- [Have I Been Pwned](https://haveibeenpwned.com/) for breach detection API
- RockYou dataset contributors
- scikit-learn community
- Flask framework developers

---

## 📞 Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Contact: cracknet@example.com

---

<div align="center">

**Made with ❤️ for Cybersecurity Education**

</div>
