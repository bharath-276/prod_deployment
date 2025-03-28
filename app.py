from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "Product_Ratings_Dataset.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df.to_dict(orient='records')
    else:
        return []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    data = load_data()
    return render_template('result.html', data=data)

@app.route('/api/data')
def get_data():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
