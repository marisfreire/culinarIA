from flask import Blueprint, render_template, url_for
from app import app

home_route = Blueprint('home', __name__) # os blueprint estão declarado, mas não estão sendo usados ainda

# rota padrão para a landingpaga
@app.route('/')
def home():
    return render_template('index.html')

new_recipe_route = Blueprint('nova_receita', __name__) # (ainda não usados)

# rota provisória para a parte de geração de recitas
@app.route('/nova_receita')
def nova_receita():
    return render_template("nova_receita.html")