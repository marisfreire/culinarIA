# arquivo para inicialização de 'app' como módulo
from flask import Flask

app = Flask(__name__)

from app.routes import home, nova_receita