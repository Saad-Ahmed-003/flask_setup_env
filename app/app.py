from flask import Blueprint

bp = Blueprint('app', __name__)

@bp.route('/')
def hello():
    return 'Hello, Flask World!'
