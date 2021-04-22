#!/usr/bin/env python3
"""[5-app.py]
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """[get_user]
    """
    try:
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request():
    """[before_request]
    """
    g.user = get_user(request.args.get('login_as'))


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
    return render_template('5-index.html')


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
