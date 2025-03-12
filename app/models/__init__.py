"""
Este módulo contém os modelos de dados da aplicação.

Classes:
    - User: Modelo para usuários
    - Recipe: Modelo para receitas
"""

from app.models.users import User
from app.models.recipes import Recipe

__all__ = ['User', 'Recipe']
