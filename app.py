from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

def load_data():
    file_path = "Product_Ratings_Dataset.csv"  # Ensure this file is in the same directory
    df = pd.read_csv(file_path)
    return df.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('result.html')

@app.route('/api/data')
def get_data():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
