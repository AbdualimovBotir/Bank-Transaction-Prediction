from flask import render_template, request, jsonify
from app import app
import pickle
import pandas as pd

# Modelni yuklash
with open('transaction_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Asosiy sahifa
@app.route('/')
def index():
    return render_template('index.html')  # HTML sahifasini qaytarish

# Bashorat qilish (Prediction)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # JSON formatida ma'lumot olish
    transaction_count = data.get('Transaction_count')
    
    # Modelni qo'llash
    prediction = model.predict([[transaction_count]])
    return jsonify({'prediction': prediction[0]})

