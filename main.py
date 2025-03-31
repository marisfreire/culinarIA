# arquivo principal para a inicialização da aplicação
from app import create_app

app, celery = create_app()

if __name__ == '__main__':
    app.run(debug=True)