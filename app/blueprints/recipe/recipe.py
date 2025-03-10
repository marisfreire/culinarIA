from flask import render_template, url_for, request
from app.blueprints.recipe import recipe_bp
import openai


# rota para a parte de geração de receitas
@recipe_bp.route('/', methods=['POST', 'GET'])
def new_recipe():
    return render_template("nova-receita/geracaodereceita.html")


# resposta para a receita 
@recipe_bp.route('/resposta', methods=['POST', 'GET'])    
def answer():
    # Função que gera a mensagem (prompt) que será enviada à API da OpenAI
    def generate_message(context:dict[str | None | bool]) -> str:
        '''Recebe o contexto como um dicionário e forma o prompt que sera mandado para a API da OpenAI'''

        message = f'Sem introduções e explicações sobre, me dê uma receita que sirva {context["porcoes"]} pessoa(as)'
        
        if context['refeicao']:
            message += f' para {context['refeicao']}'

        if context['culinaria']:
            message += f', ela deve ser da culinaria {context['culinaria']}'

        if context['restricoes']:
            message += f', a receita NÃO pode conter {context['restricoes']}'

        if context['ingredientes']:
            apenas = 'use apenas esses ingredientes e nenhum outro' if context['apenas_ingredientes'] else 'se necessário pode usar outros ingredientes'
            message += f', ela deve usar os seguintes ingredientes: {context["ingredientes"]}, {apenas}'

        if context['eletrodomesticos']:
            message += f', se necessário, de preferência use apenas os seguintes eletrodomésticos: {context['eletrodomesticos']}'

        return message

    if request.method == "POST":
        data = request.json # recebe os dados do front
        context = {
            'ingredientes':        data.get('ingredientes'),
            'eletrodomesticos':    data.get('eletrodomesticos'),
            'restricoes':          data.get('restricoes'),
            'culinaria':           data.get('culinaria'),
            'porcoes':             data.get('porcoes'),
            'refeicao':            data.get('refeicao'),
            'apenas_ingredientes': data.get('apenas_ingredientes')
        }
        

    # Função para gerar a resposta usando a API da OpenAI
    def generate(message:str):
        import dotenv, os
        dotenv.load_dotenv(dotenv.find_dotenv())
        openai.api_key = os.getenv("API_KEY")

        stream = openai.chat.completions.create(
            model="gpt-4o-mini", # talvez mudar o modelo para um mais preciso antes do 'deploy' seja interessante
            messages=[{"role": "user", "content": message}],
            stream=True,
            max_tokens=50 # poucos tokens apenas para testes, normalmente 400 - 500 é suficente
        ) 

        for chunk in stream: # stream da resposta
            if chunk.choices[0].delta.content is not None:
                yield(chunk.choices[0].delta.content)

    return generate(generate_message(context=context)), {"Content-Type": "text/plain"}
