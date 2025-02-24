from flask import Blueprint, render_template
from app.blueprints.menu import menu_bp
# from flask_login import login_required, current_user
# from app.models.users import User
# from app.models.favorites import Favorite

@menu_bp.route('/')
def menu():
    return render_template('menu/menu.html')
