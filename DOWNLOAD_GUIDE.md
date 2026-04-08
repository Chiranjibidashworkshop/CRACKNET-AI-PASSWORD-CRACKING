# 📦 CrackNet - Complete Download Guide

## 🗂️ Files to Download

Download the entire `/app` directory with the following structure:

### Complete File List:

```
/app/
├── 📄 README.md                          ⬇️ DOWNLOAD
├── 📄 QUICKSTART.md                      ⬇️ DOWNLOAD
├── 📄 USAGE_GUIDE.md                     ⬇️ DOWNLOAD
├── 📄 PROJECT_SUMMARY.md                 ⬇️ DOWNLOAD
├── 📄 requirements.txt                   ⬇️ DOWNLOAD
├── 📄 .env                               ⬇️ DOWNLOAD
│
├── 📁 src/                               ⬇️ DOWNLOAD ENTIRE FOLDER
│   ├── 📄 clean_data.py
│   ├── 📄 train_model.py
│   │
│   ├── 📁 app/
│   │   ├── 📄 app.py
│   │   │
│   │   ├── 📁 features/
│   │   │   └── 📄 utils.py
│   │   │
│   │   ├── 📁 templates/
│   │   │   └── 📄 index.html
│   │   │
│   │   └── 📁 static/
│   │       ├── 📁 css/
│   │       │   └── 📄 style.css
│   │       └── 📁 js/
│   │           └── 📄 main.js
│   │
│   └── 📁 simulator/
│       └── 📄 crack_time.py
│
├── 📁 data/                              ⬇️ DOWNLOAD ENTIRE FOLDER
│   ├── 📁 raw/                           (empty - for your datasets)
│   └── 📁 processed/
│       └── 📄 cleaned_passwords.csv
│
└── 📁 models/                            ⬇️ DOWNLOAD ENTIRE FOLDER
    ├── 📄 password_model.pkl
    └── 📄 label_encoder.pkl
```

---

## 📋 File Count Summary

- **Python Files:** 8 files
- **HTML Files:** 1 file
- **CSS Files:** 1 file
- **JavaScript Files:** 1 file
- **Documentation Files:** 4 files
- **Configuration Files:** 2 files (.env, requirements.txt)
- **Data Files:** 1 file (cleaned_passwords.csv)
- **Model Files:** 2 files (.pkl files)

**Total: 20 files + folder structure**

---

## 🎯 Essential Files You MUST Download

### 1️⃣ Documentation (4 files)
- README.md
- QUICKSTART.md
- USAGE_GUIDE.md
- PROJECT_SUMMARY.md

### 2️⃣ Configuration (2 files)
- requirements.txt
- .env

### 3️⃣ Source Code (8 Python files)
- src/clean_data.py
- src/train_model.py
- src/app/app.py
- src/app/features/utils.py
- src/simulator/crack_time.py

### 4️⃣ Frontend (3 files)
- src/app/templates/index.html
- src/app/static/css/style.css
- src/app/static/js/main.js

### 5️⃣ Trained Models (2 files)
- models/password_model.pkl
- models/label_encoder.pkl

### 6️⃣ Data (1 file)
- data/processed/cleaned_passwords.csv

---

## 💾 How to Download

### Option 1: Download Individual Files
Click on each file in the file explorer and download them one by one.

### Option 2: Download as ZIP (Recommended)
If your platform supports it, download the entire `/app` folder as a ZIP archive.

### Option 3: Use File Explorer
Navigate to `/app` in the file explorer and download the entire directory.

---

## 📂 Folder Structure to Create Locally

After downloading, ensure this structure on your local machine:

```
CrackNet/
├── README.md
├── QUICKSTART.md
├── USAGE_GUIDE.md
├── PROJECT_SUMMARY.md
├── requirements.txt
├── .env
├── src/
│   ├── app/
│   │   ├── features/
│   │   ├── templates/
│   │   └── static/
│   │       ├── css/
│   │       └── js/
│   └── simulator/
├── data/
│   ├── raw/
│   └── processed/
└── models/
```

---

## ✅ Verification Checklist

After downloading, verify you have:

- [ ] All 8 Python files
- [ ] HTML template file
- [ ] CSS stylesheet
- [ ] JavaScript file
- [ ] 4 documentation files
- [ ] requirements.txt
- [ ] .env file
- [ ] 2 model .pkl files
- [ ] cleaned_passwords.csv
- [ ] Proper folder structure

---

## 🚀 Quick Setup After Download

1. Extract files (if downloaded as ZIP)
2. Open folder in VSCode: `code /path/to/CrackNet`
3. Create virtual environment: `python -m venv venv`
4. Activate: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Run application: `python src/app/app.py`
7. Access: http://localhost:5000

---

## 📊 File Sizes

- **Total Project Size:** ~250 KB
  - Models: ~210 KB
  - Data: ~150 KB (varies)
  - Code: ~100 KB
  - Documentation: ~50 KB

---

## ⚠️ Important Notes

1. **Don't forget the .env file** - Contains important configuration
2. **Download both .pkl model files** - Required for ML functionality
3. **Keep folder structure intact** - Application expects specific paths
4. **data/raw/ folder is empty** - This is normal (for your own datasets)

---

## 🎓 Optional: Add Your Own Dataset

If you have the RockYou.txt dataset:
1. Place it in `data/raw/rockyou.txt`
2. Run: `python src/clean_data.py`
3. Run: `python src/train_model.py`
4. This will retrain the model with more data

---

**Ready to download! All files are in `/app` directory.**
