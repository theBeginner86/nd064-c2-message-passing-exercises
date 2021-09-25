import json
from flask import Flask, jsonify, request
from .enums import Status

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'response': 'Hello World!'})


@app.route('/orders/create_order', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        return jsonify(create_order(request_body))
    else:
        raise 'Unwanted HTTP request!! Try Again...'


if __name__ == '__main__':
    app.run()
