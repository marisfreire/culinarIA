from flask import Blueprint, render_template, url_for, request, redirect
from app import app
from openai import OpenAI

OpenAI.api_key = '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'

# não implementar por enquanto
'''def generatePrompt(mensagem:str) -> str:
    
 
def generateMensage(context:dict[str | None]) -> str:

    mensage = f'me dê uma receita para {context["tipo"]}'
    
    if context['gastronomia']:
        mensage += f', ela deve ser da gastronomia {context['gastronomia']}'

    if context['restricoes']:
        mensage += f', a receita NÃO pode conter {context['restricoes']}'

    if context['ingredientes']:
        mensage += f', a deve usar os seguintes ingredientes: {context["ingredientes"]}'

    return generatePrompt(mensage)'''
    


home_route = Blueprint('home', __name__) # os blueprint estão declarado, mas não estão sendo usados ainda
# rota padrão para a landingpaga
@app.route('/')
def home():
    return render_template('index.html')


new_recipe_route = Blueprint('nova-receita', __name__) # (ainda não usados)
# rota provisória para a parte de geração de recitas
@app.route('/nova-receita')
def novaReceita():

    if request.method == "GET":
        context = {'tipo':request.args.get('tipo', None), # valor padrão será None
                   'restricoes':request.args.get('restricoes', None), 
                   'ingredientes':request.args.get('ingredientes', None), 
                   'gastronomia':request.args.get('gastronomia', None)}
    
    if context['tipo']:
        # mensage = generateMensage(context=context)
        return redirect(url_for('loadingPage'))
    
    return render_template("nova_receita.html")


@app.route('/nova-receita/gerando')
def loadingPage():
    return "carregando..."