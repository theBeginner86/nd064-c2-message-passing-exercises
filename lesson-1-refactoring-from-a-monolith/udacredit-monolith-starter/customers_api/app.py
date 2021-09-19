from flask import Flask, jsonify, make_response
from .services.customers import get_customers

app = Flask(__name__)


@app.route('/customers', methods=['GET'])
def customers():
    response = {
        "customers": get_customers()
    }
    response = make_response(jsonify(response))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response
