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
    scaler = joblib.load(scaler_path)
    data = load_data_from_csv(file_path, max_length)
    data = scaler.transform(data.reshape(-1, data.shape[-1])).reshape(data.shape)
    predictions = model.predict(data)
    return predictions

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    max_length = int(request.form.get('max_length', 51))
    predictions = predict_single_csv(file_path, max_length)
    os.remove(file_path)  # Clean up the uploaded file after processing
    print(predictions)
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
