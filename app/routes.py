from flask import render_template, url_for, request, Response
from app import app
import os
import dotenv
import openai

dotenv.load_dotenv(dotenv.find_dotenv()) # carrega as variaveis de ambiente

openai.api_key = os.getenv("API_KEY") 


def generate_message(context:dict[str | None]) -> str:
    '''Recebe o contexto como um dicionário e forma o prompt que sera mandado para a api do chat gpt'''
    message = f'me dê uma receita para {context["tipo"]}' # o tipo é obrigatorio, então sempre será retornado
    
    if context['gastronomia']:
        message += f', ela deve ser da gastronomia {context['gastronomia']}'

    if context['restricoes']:
        message += f', a receita NÃO pode conter {context['restricoes']}'

    if context['ingredientes']:
        message += f', a deve usar os seguintes ingredientes: {context["ingredientes"]}'

    return message


# rota padrão para a página inicial
@app.route('/')
def home():
    return render_template('index.html')


# rota para a parte de geração de receitas
@app.route('/nova-receita')
def nova_receita():
    return render_template("nova_receita.html")


@app.route('/resposta', methods=['POST', 'GET'])
def answer():

    if request.method == "POST":
        data = request.json
        context = {
            'tipo': data.get('tipo'),
            'restricoes': data.get('restricoes'),
            'ingredientes': data.get('ingredientes'),
            'gastronomia': data.get('gastronomia')
        }

        message = generate_message(context=context)

    def generate(): 
        response = openai.completions.create(
            model="gpt-4o-mini",
            prompt=message,
            max_tokens=100,
            stream=True) 

        for chunk in response:
            if chunk.get("choices"):
                yield chunk["choices"][0].get("text", "")

    return Response(generate(), content_type="text/plain")