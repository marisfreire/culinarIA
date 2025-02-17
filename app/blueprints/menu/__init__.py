from flask import Blueprint

home_bp = Blueprint('home', __name__, url_prefix='/')

from app.blueprints.home import routes