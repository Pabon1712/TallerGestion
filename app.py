from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('modelo_pokemon.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    stats = [
        float(request.form['hp']),
        float(request.form['attack']),
        float(request.form['defense']),
        float(request.form['sp_atk']),
        float(request.form['sp_def']),
        float(request.form['speed'])
    ]
    
    stats_np = np.array([stats])
    prediction = model.predict(stats_np)[0]
    probability = model.predict_proba(stats_np)[0][1]

    return render_template('result.html', 
                           prediction=prediction, 
                           probability=round(probability * 100, 2))

if __name__ == '__main__':
    app.run(debug=True)
