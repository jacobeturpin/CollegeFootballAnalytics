from flask import Blueprint, json
from json import dumps

mod = Blueprint('api', __name__, url_prefix='/api')

@mod.route('/test')
def index():
    return dumps(['Test', 'Successful'])