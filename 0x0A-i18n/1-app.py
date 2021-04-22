#!/usr/bin/env python3
"""[1-app.py]
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """[Config]
    """
    LANGUAGES = ['en', 'es']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_holberton() -> str:
    """[welcome holberton endpoint]
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
