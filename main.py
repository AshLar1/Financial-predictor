from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load('stacked_model_60.pkl')
scaler = joblib.load('standard_scaler.pkl')

FEATURES = [
    'ROA(C) before interest and depreciation before interest',
    'ROA(A) before interest and % after tax',
    'ROA(B) before interest and depreciation after tax', 'Current Ratio',
    'Total debt/Total net worth', 'Debt ratio %', 'Net worth/Assets',
    'Equity to Liability'
]

THRESHOLD = 0.3  # Ensure the model is using the correct threshold


@app.route('/')
def home():
  return render_template('index.html', prediction=None)


@app.route('/predict', methods=['POST'])
def predict():
  try:
    # Get user input and convert to DataFrame
    data = [float(request.form.get(feature)) for feature in FEATURES]
    df = pd.DataFrame([data], columns=FEATURES)

    # Scale the input
    scaled_data = scaler.transform(df)

    # Get probability from the model
    probability = model.predict_proba(scaled_data)[0][1]

    # Determine prediction output
    if probability >= THRESHOLD:
      feedback = f"⚠️ High Risk of Bankruptcy. Probability: {probability:.2f}"
    else:
      feedback = f"✅ Low Risk of Bankruptcy. Probability: {probability:.2f}"

    return render_template('index.html', prediction=feedback)

  except Exception as e:
    return f"Error: {e}"


app.run(host='0.0.0.0', port=3000)
