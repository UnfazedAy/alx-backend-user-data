#!/usr/bin/env python3
"""The basic flask app module"""

from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def root():
    """GET the root or home page"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route("/users", methods=['POST'], strict_slashes=False)
def register():
    """A method to register users"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": f"{user.email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login():
    """Handles login sessions"""
    email = request.form.get('email')
    password = request.form.get('password')

    valid_user_login = AUTH.valid_login(email, password)

    if valid_user_login:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response

    abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """The logout method"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for('root'))

    abort(403)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile():
    """View to handle the user profile"""
    try:
        session_id = request.cookies.get('session_id')
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": f"{user.email}"}), 200

    except Exception:
        abort(403)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
