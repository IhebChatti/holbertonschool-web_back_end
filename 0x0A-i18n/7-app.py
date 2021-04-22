#!/usr/bin/env python3
"""[6-app.py]
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

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
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    """[get_locale]
    """
    locale = request.args.get('locale')
    if locale:
        return locale
    user = request.args.get('login_as')
    if user:
        user_lang = users.get(int(user).get('locale'))
        if user_lang in app.config['LANGUAGES']:
            return user_lang
    headers = request.headers.get('locale')
    if headers:
        return headerss
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """[get_timezone]
    """
    try:
        timezone = request.args.get("timezone")
        if timezone:
            return pytz.timezone(timezone)
        user = request.args.get('login_as')
        if user:
            timezone = users.get(int(user).get('timezone'))
            if timezone:
                return pytz.timezone(timezone)
        timezone = request.headers.get('timezone')
        if timezone:
            return pytz.timezone(timezone)

    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
