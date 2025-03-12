from flask import render_template, request, jsonify
from app.blueprints.recipe import recipe_bp
from flask_login import current_user
import openai
import json
import re


# rota para a parte de geração de receitas
@recipe_bp.route('/', methods=['POST', 'GET'])
def new_recipe():
    return render_template("nova-receita/nova-receita.html")


# resposta para a receita 
@recipe_bp.route('/resposta', methods=['POST'])
def response():
    def generate_message(context):
        message = f'''Me forneça uma receita em formato JSON, apenas isso, sem nenhum comentário ou frase, com os seguintes campos: 
        'titulo', 'dificuldade', 'tempo_de_preparo', 'tipo_de_refeicao', 'ingredientes' (lista de objetos com 'nome' e 'quantidade'), 
        e 'passos' (lista de instruções numeradas).
        Ela deve servir {context["porcoes"]} pessoa(s)'''
        
        if not context['nao_informa_refeicao'] and context['refeicao']:
            message += f', será uma receita para {context["refeicao"]}'

        if not context['nao_informa_culinaria'] and context['culinaria']:
            message += f', ela deve ser da culinaria {context["culinaria"]}'

        if context['ingredientes']:
            apenas = 'use apenas esses ingredientes e nenhum outro, ' if context['apenas_ingredientes'] else 'se necessário pode usar outros ingredientes, '
            message += f', ela deve usar os seguintes ingredientes: {context["ingredientes"]}, {apenas}'

        if current_user.is_authenticated:
            restrictions = current_user.preferences['dietary_restrictions']
            skill_level = current_user.preferences['skill_level']
            
            if restrictions:
                restrictions_str = ', '.join(restrictions)
                message += f', a receita NÃO pode conter {restrictions_str}'
            
            message += f', a receita deve ser para alguém de nível {skill_level}'

        message += f', o tempo de preparo deve ser de aproximadamente {context["tempo"]} minutos'
        
        return message

    if request.method == "POST":
            data = request.get_json()
            message = generate_message(data)
            
            import dotenv, os
            dotenv.load_dotenv(dotenv.find_dotenv())
            client = openai.OpenAI(api_key=os.getenv("API_KEY"))

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": message}],
                temperature=0.7,
            )
            # para acessar a resposta corretamente na API
            response_content = response.choices[0].message.content
            # tirar "```json" do markdown para transformar em json
            cleaned_content = re.sub(r"^```json|```$", "", response_content).strip()

            recipe_data = json.loads(cleaned_content) if cleaned_content else {}

            return jsonify(recipe_data)