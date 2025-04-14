from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cars = []

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars), 200

@app.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    if not all(k in data for k in ('make', 'year', 'price')):
        return jsonify({'error': 'Missing car data'}), 400

    car = {
        'id': len(cars) + 1,
        'make': data['make'],
        'year': data['year'],
        'price': data['price']
    }

    cars.append(car)
    return jsonify(car), 201

if __name__ == '__main__':
    app.run(debug=True)
