from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def data():
    data = request.get_json()
    user_input = data.get('userInput', '')
    stored_data = user_input  # Store the data
    response_data = {'message': f'Stored Data: {stored_data}'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
