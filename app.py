from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get', methods=['GET'])
def get_request():
    return jsonify({'message': 'GET request received'})

@app.route('/post', methods=['POST'])
def post_request():
    data = request.get_json()
    return jsonify({'message': 'POST request received', 'data': data})

@app.route('/put', methods=['PUT'])
def put_request():
    data = request.get_json()
    return jsonify({'message': 'PUT request received', 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
