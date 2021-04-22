#!/usr/bin/env python3
"""[4-app.py]
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """[Config]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome_holberton() -> str:
    """[welcome holberton endpoint]
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """[get_locale]
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
