from flask import Blueprint
import flask
from app.task.models import * 

task = Blueprint('task', __name__)
app = flask.current_app

@task.route('/tasks', methods=['GET'])
def show_all_tasks():
    todo = Todo()
    print (todo.title)
