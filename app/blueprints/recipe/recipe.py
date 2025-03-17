from flask import render_template, request, jsonify
from app.blueprints.recipe import recipe_bp
from flask_login import current_user
import openai
import json
import re
from flask_login import login_required
from app.models import Recipe


# rota para a parte de geração de receitas
@recipe_bp.route('/', methods=['POST', 'GET'])
def new_recipe():
    return render_template("nova-receita/nova-receita.html")


# gera o prompt
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


# resposta para a receita 
@recipe_bp.route('/resposta', methods=['POST'])
def response():
    if request.method == "POST":
        try:
            # Primeiro, tenta fazer o parse do JSON
            if not request.is_json:
                return jsonify({"error": "Requisição deve ser JSON"}), 400
            
            try:
                data = request.get_json()
            except Exception:
                return jsonify({"error": "JSON inválido"}), 400

            if data is None:
                return jsonify({"error": "JSON inválido"}), 400
            
            # Validar campos obrigatórios
            required_fields = ['porcoes', 'tempo', 'ingredientes']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
            
            message = generate_message(data)
            
            import dotenv, os
            dotenv.load_dotenv(dotenv.find_dotenv())
            client = openai.OpenAI(api_key=os.getenv("API_KEY"))

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": message}],
                temperature=0.7,
            )
            
            response_content = response.choices[0].message.content
            cleaned_content = re.sub(r"^```json|```$", "", response_content).strip()
            
            try:
                recipe_data = json.loads(cleaned_content) if cleaned_content else {}
                recipe_id = Recipe.get_next_recipe_id()
                recipe_data['recipe_id'] = recipe_id
                
                # criar a receita no banco
                Recipe.create_recipe(
                    title=recipe_data['titulo'],
                    ingredients=recipe_data['ingredientes'],
                    instructions=recipe_data['passos'],
                    difficulty=recipe_data['dificuldade'],
                    time=recipe_data['tempo_de_preparo'],
                    meal_type=recipe_data['tipo_de_refeicao']
                )
                
                return jsonify(recipe_data)
            except json.JSONDecodeError:
                return jsonify({"error": "Erro ao processar resposta da API"}), 500

        except json.JSONDecodeError:
            return jsonify({"error": "JSON inválido"}), 400
        except KeyError as e:
            return jsonify({"error": f"Campo obrigatório ausente: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Método não permitido"}), 405


@recipe_bp.route('/favorito/<int:recipe_id>', methods=['POST'])
@login_required
def toggle_favorite(recipe_id):
    try:
        recipe = Recipe.find_by_id(recipe_id)
        if not recipe:
            return jsonify({"error": "Receita não encontrada"}), 404
        
        if hasattr(current_user, 'favorites_recipes_id') and current_user.favorites_recipes_id is not None:
            is_favorite = recipe_id in current_user.favorites_recipes_id
        else:
            is_favorite = False
            
        if is_favorite:
            current_user.remove_favorite_recipe(recipe_id)
        else:
            current_user.add_favorite_recipe(recipe_id)
            
        return jsonify({
            "status": "success",
            "is_favorite": not is_favorite
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500