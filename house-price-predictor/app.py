from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    size = float(request.form['size'])
    prediction = model.predict([[size]])
    return render_template('index.html', result=f'Predicted Price: ₹{prediction[0]:.2f} lakhs')

if __name__ == '_main_':
    app.run(debug=True)