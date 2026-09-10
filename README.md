# 🛡️ ScamGuard AI

AI-powered scam detection web application that analyzes suspicious messages and screenshots to identify potential scams and provide immediate safety recommendations.

## 📌 Overview

ScamGuard AI is a Machine Learning based web application designed to help users identify potentially fraudulent or suspicious messages.

The application can analyze:

- SMS messages
- WhatsApp messages
- Emails
- Suspicious text
- Screenshots of suspicious messages
- Suspicious URLs

After analysis, ScamGuard AI provides a **Risk Score**, **Risk Level**, **Scam Type**, reasons why the message was flagged, and recommended safety actions.

> ScamGuard AI provides a risk assessment only. It does not prove that a message is fraudulent or provide legal advice.

---

## ✨ Features

### 🔍 Text Scam Detection

Users can paste suspicious text into the application and receive an AI-based risk assessment.

### 📸 Screenshot Scam Detection

Users can upload a screenshot of a suspicious message.

The application uses OCR to:

1. Extract text from the screenshot
2. Analyze the extracted text
3. Generate the scam detection report

The extracted OCR text is processed internally and is not displayed to the user.

### 📊 Risk Assessment

The application generates a Risk Score and Risk Level.

| Risk Score | Risk Level |
|------------|------------|
| 0–30 | Low Risk |
| 31–70 | Suspicious |
| 71–100 | High Risk |

> The Risk Score is an assessment score and should not be interpreted as a calibrated probability.

### 🏷️ Scam Type Detection

The application identifies possible scam categories such as:

- Banking / KYC Scam
- UPI / Payment Scam
- Job Scam
- Lottery Scam
- Courier Scam
- Electricity Scam
- Investment Scam
- Loan Scam
- Phishing

### 🚨 Why Flagged?

The application explains common warning signs detected in the message, such as:

- Urgency or pressure
- OTP requests
- Suspicious URLs
- Account threats
- Impersonation
- Payment requests

### 🛡️ Recommended Actions

ScamGuard AI provides immediate safety advice based on the detected risk level.

For example:

- Do not click suspicious links
- Do not share OTP, PIN, CVV or passwords
- Do not make payments under pressure
- Verify the sender through official channels
- Preserve relevant evidence

### 🔗 URL Analysis

Suspicious URLs are analyzed for common warning signs such as unusual domains and potentially risky patterns.

### 🚨 Take Action

The application provides official cybercrime reporting information and guidance for users who may have encountered a scam.

### 🗄️ Scan History

Authenticated users can save their scan results to Supabase and retrieve previous scan history.

### 🔐 Authentication

Email-based Signup and Login are implemented using Supabase Authentication.

---

## 🧠 Machine Learning

ScamGuard AI currently uses:

- **TF-IDF Vectorization**
- **Logistic Regression**

The ML model was trained using the **UCI SMS Spam Collection** dataset.

### Model Performance

Current evaluation results:

| Metric | Score |
|--------|-------|
| Accuracy | 98.21% |
| Precision | 92.16% |
| Recall | 94.63% |
| F1 Score | 93.38% |

These results are based on the current dataset and evaluation setup.

The model should be considered a baseline and cannot detect every type of modern scam.

---

## 🔄 Application Workflow

### Text Analysis

```text
User enters suspicious text
        ↓
Text preprocessing
        ↓
TF-IDF Vectorization
        ↓
Machine Learning Model
        ↓
Risk Engine
        ↓
Scam Type + URL Analysis
        ↓
Scam Detection Report
        ↓
Recommended Actions
        ↓
Save result to Supabase

Screenshot Analysis

User uploads screenshot
        ↓
OCR using Tesseract
        ↓
Extracted text
        ↓
Scam Detection Pipeline
        ↓
Risk Assessment
        ↓
Scam Detection Report
        ↓
Recommended Actions
        ↓
Save result to Supabase

🛠️ Tech Stack

Frontend / Application
Python
Streamlit


Machine Learning
Scikit-learn
TF-IDF
Logistic Regression
Pandas
OCR
Tesseract OCR
Pytesseract
Pillow


Database & Authentication

Supabase
PostgreSQL
Supabase Authentication
Row Level Security (RLS)

Other Tools


HTTPX
Python-dotenv
Git
GitHub
VS Code


 Project Structure
scamguard-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── ml/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── models/
│   ├── scam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── services/
│   ├── ocr.py
│   ├── url_analyzer.py
│   ├── risk_engine.py
│   ├── scam_classifier.py
│   ├── legal_info.py
│   └── recommendations.py
│
├── database/
│   └── supabase_client.py
│
├── utils/
│   ├── text_cleaner.py
│   └── validators.py
│
├── assets/
│   └── logo.png
│
└── screenshots/


Project Status

ScamGuard AI is an actively developed college/portfolio project.

Core features including Machine Learning based detection, screenshot OCR, URL analysis, Supabase authentication, scan history, and safety recommendations are implemented.

Author

Vansh Gupta

B.Tech Computer Science & Engineering