# 📊 Business Bankruptcy Predictor

This web app predicts the financial stability of a business using AI. It takes in financial ratios and outputs a prediction of whether a business is likely to go bankrupt.

🔗 **Live App (via Replit):** [Launch the App](https://replit.com/@ashleylartey/Financial-predictor)

---

## 🚀 Features

- Built using **Flask**, styled with **HTML/CSS**
- Accepts financial input (ROA, Debt Ratio, Equity-to-Liability, etc.)
- Uses a trained **machine learning model** (`stacked_model_60.pkl`)
- Standardized using `StandardScaler`
- Hosted on **Replit**

---

## 🧠 Model Details

- Model: Stacking Classifier (RandomForest + Logistic Regression)
- Accuracy: **~82%**
- Features: ROA (A, B, C), Debt Ratio %, Equity/Liability, Current Ratio

---

## 📁 File Structure
├── main.py # Flask app logic
├── static/style.css # CSS styling
├── templates/index.html # Frontend UI
├── stacked_model_60.pkl # Trained ML model
├── standard_scaler.pkl # Scaler used during training

---

## 📦 Requirements

Install dependencies:

```bash
pip install flask scikit-learn pandas

---

**👨‍💻 How to Run Locally**

```bash
python main.py
App runs at: http://localhost:5000

---

✨ Author
Ashley Lartey – LinkedIn - https://www.linkedin.com/in/ashleylartey/
