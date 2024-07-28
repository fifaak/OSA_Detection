# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from catboost import CatBoostClassifier
import joblib
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config['UPLOAD_FOLDER'] = 'uploads'  # Directory to store uploaded files
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

MODEL_PATH = '../model2/catboost_model.cbm'
SCALER_PATH = '../model2/scaler.pkl'

state = 0  # Initialize the state variable

def load_data_from_csv(file_path, max_length):
    df = pd.read_csv(file_path)
    df.columns = ['sec', 'temp']
    temp_values = df['temp'].values
    data = [temp_values]
    data = pad_sequences(data, maxlen=max_length, dtype='float32', padding='post', truncating='post')
    return np.array(data)

def predict_single_csv(file_path, max_length, model_path=MODEL_PATH, scaler_path=SCALER_PATH):
    model = CatBoostClassifier()
    model.load_model(model_path)
    df = pd.read_csv(file_path)

    scaler = joblib.load(scaler_path)
    data = load_data_from_csv(file_path, max_length)
    data = scaler.transform(data.reshape(-1, data.shape[-1])).reshape(data.shape)
    predictions = model.predict(data)
    if (predictions[0] == 1 or ((df['temp'].max() - df['temp'].min()) < 0.5)):
        predictions[0] = 1
    return predictions

def warning():
    print("warning")

def sos():
    print("sos")

def workflow(csv_path):
    global state  # Ensure state is recognized as a global variable

    pred = predict_single_csv(csv_path, max_length=51)
    if (pred == 1 and state == 0):
        warning()
        state = 1
        return "Warning"
    elif (pred == 1 and state == 1):
        sos()
        state = 2
        return "SOS"
    elif (pred == 0 and state == 1):
        state = 0
        return "Normal"
    else:
        state = 2
        return "SOS!"

@app.route('/predict', methods=['POST'])
def predict():
    global state  # Use the global state variable

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    new_state = workflow(file_path)
    os.remove(file_path)  # Clean up the uploaded file after processing
    
    return jsonify({'state': new_state})

if __name__ == '__main__':
    app.run(debug=True)
