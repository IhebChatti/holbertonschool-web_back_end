#!/usr/bin/env python3
"""[session auth view]
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login',
                 methods=['POST'],
                 strict_slashes=False)
def login():
    """[login]
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    if user[0].is_valid_password(pwd):
        from api.v1.app import auth
        session_user = auth.create_session(user[0].id)
        res = jsonify(user[0].to_json())
        res.set_cookie(os.getenv("SESSION_NAME"), session_user)
        return res
    else:
        return jsonify({"error": "wrong password"}), 401
