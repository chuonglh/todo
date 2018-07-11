from flask import Flask, request, g
from flask_mongoalchemy import MongoAlchemy
from http import HTTPStatus


def init_app(name=__name__, settings_override=None):
    """This is init Flask app"""
    app = Flask(name, instance_relative_config=True)
    # Loading config file in instance folder
    load_config(app, settings_override)

    # Register blue print
    from app.health_check.api import hc
    app.register_blueprint(hc, url_prefix='/v1')
    from app.task.api import task
    app.register_blueprint(task, url_prefix='/v1')

    # in App Context
    with app.app_context():
        if not hasattr(g, 'db'):
            g.db = connect_db(app)

    # Load function before request
    app.before_request(before_request)

    return app


def load_config(app, settings_override):
    """Loading"""
    app.config.from_pyfile('config.py')
    if settings_override:
        app.config.update(settings_override)


def connect_db(app):
    # Init DB Mongo
    db = MongoAlchemy(app)
    return db


def get_db():
    return g.db


def before_request():
    """HTTP method"""
    if request.method == 'OPTIONS':
        return {}, HTTPStatus.OK.value
