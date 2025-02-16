# arquivo principal para a inicialização da aplicação
from app import crate_app

app = crate_app()

if __name__ == '__main__':
    app.run(debug=True)