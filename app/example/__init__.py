from sys import prefix
from flask import Blueprint
example_bp = Blueprint('example', __name__, template_folder='templates')
from . import views