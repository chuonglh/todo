import json
from flask import Blueprint
from http import HTTPStatus
from flask import Response
import flask
from app.core import connect_db
from mongoalchemy.session import Session


hc = Blueprint('health_check', __name__)
app = flask.current_app

@hc.route('/health_check', methods=['GET', 'HEAD'])
def health_check():
    try:
        #session = Session.connect('library', host=app.config['MONGO_URI'])
        session = Session.connect(app.config['MONGOALCHEMY_DATABASE'])
    except Exception as e:
        return Response(str(e.args[0]), status=HTTPStatus.INTERNAL_SERVER_ERROR.value)
    data = json.dumps({'msg': 'Still alive'})
    resp = Response(data, status=HTTPStatus.OK.value, mimetype='application/json')
    return resp
