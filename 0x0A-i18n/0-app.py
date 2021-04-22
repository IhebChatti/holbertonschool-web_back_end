#!/usr/bin/env python3
"""[0-app.py]
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.rout('/', methods=['GET'], strict_slashes=False)
def welcome_holberton() -> str:
    """[welcome holberton endpoint]
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(0.0.0.0, 5000)
