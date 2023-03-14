#!/usr/bin/env python3
"""The basic flask app module"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def root():
    """GET the root or home page"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
