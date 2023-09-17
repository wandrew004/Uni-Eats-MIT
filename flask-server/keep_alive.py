from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from main import find_combinations_within_margin
from webscraper import import_food



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
    stored_data =int(stored_data)
    foodList = import_food()
    print(stored_data, type(stored_data))
    print(find_combinations_within_margin(foodList, stored_data, 100))
    return find_combinations_within_margin(foodList, stored_data, 100)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
