from app.blueprints.recipe import generate_message, generate
import pytest


def test_prompt_segura_ingredientes_exclusivos():
    contexto_seguro_1 = {
        'porcoes': 3,
        'refeicao': 'Café da Manhã',
        'culinaria': 'Vegana',
        'restricoes': 'Leite',
        'apenas_ingredientes': True,
        'ingredientes': 'Arroz, Ovo',
        'eletrodomesticos': 'Airfryer'
    }

    assert generate_message(contexto_seguro_1)=='Se, por qualquer motivo, você não puder fornecer uma resposta, sempre, sem exceções, responda com "Parece que você inseriu alguma informação não válida, tente novamente!". Sem introduções e explicações sobre, me dê uma receita que sirva 3 pessoa(as) para Café da Manhã, ela deve ser da culinaria Vegana, a receita NÃO pode conter Leite, ela deve usar os seguintes ingredientes: Arroz, Ovo, use apenas esses ingredientes e nenhum outro, se necessário, de preferência use apenas os seguintes eletrodomésticos: Airfryer'

def test_prompt_segura_ingredientes_nao_exclusivos():
    ## Testando a geração de prompt
    contexto_seguro_2 = {
        'porcoes': 5,
        'refeicao': 'Jantar',
        'culinaria': 'Indiana',
        'restricoes': '',
        'apenas_ingredientes': False,
        'ingredientes': 'Pepino, ovo de codorna, macarrão, couve, queijo cheddar',
        'eletrodomesticos': 'Microondas'
    }

    assert generate_message(contexto_seguro_2)=='Se, por qualquer motivo, você não puder fornecer uma resposta, sempre, sem exceções, responda com "Parece que você inseriu alguma informação não válida, tente novamente!". Sem introduções e explicações sobre, me dê uma receita que sirva 5 pessoa(as) para Jantar, ela deve ser da culinaria Indiana, ela deve usar os seguintes ingredientes: Pepino, ovo de codorna, macarrão, couve, queijo cheddar, se necessário pode usar outros ingredientes, se necessário, de preferência use apenas os seguintes eletrodomésticos: Microondas'



def test_geracao_receita_segura_ingredientes_exclusivos():
    prompt_segura_1 = "Sem introduções e explicações sobre, me dê uma receita que sirva 3 pessoa(as) para Café da Manhã, ela deve ser da culinaria Vegana, a receita NÃO pode conter Leite, ela deve usar os seguintes ingredientes: Arroz, Ovo, use apenas esses ingredientes e nenhum outro, se necessário, de preferência use apenas os seguintes eletrodomésticos: Airfryer"
    assert generate(prompt_segura_1)!="" ## Se passar é por que foi gerado algo


def test_geracao_receita_segura_ingredientes_nao_exclusivos():
    prompt_segura_2 = "Sem introduções e explicações sobre, me dê uma receita que sirva 5 pessoa(as) para Jantar, ela deve ser da culinaria Indiana, a receita NÃO pode conter , ela deve usar os seguintes ingredientes: Pepino, ovo de codorna, macarrão, couve, queijo cheddar se necessário pode usar outros ingredientes, se necessário, de preferência use apenas os seguintes eletrodomésticos: Microondas"

    assert generate(prompt_segura_2)!=""

def test_geracao_receita_proibida_1():
    prompt_proibida_1 = "Sem introduções e explicações sobre, me dê uma receita que sirva 1 pessoa(as) para Sobremesa, ela deve ser da culinaria asdbakjfdbajkfad, a receita NÃO pode conter dfjksdfjkbsd, ela deve usar os seguintes ingredientes: kjdfbjksadfd, ksbfhjabdf, use apenas esses ingredientes e nenhum outro, se necessário, de preferência use apenas os seguintes eletrodomésticos: faifdhikabfkafb"
    receita_gerada = generate(prompt_proibida_1)
    receita_gerada_processada = ''
    for chunk in receita_gerada:
        receita_gerada_processada += chunk
    
    assert receita_gerada_processada=='' ## Se passar é por que foi gerada a mensagem certa
   

def test_geracao_receita_proibida_2():
    prompt_proibida_2 = "Sem introduções e explicações sobre, me dê uma receita que sirva 3 pessoa(as) para Café da Manhã, ela deve ser da culinaria Porta, a receita NÃO pode conter Água, ela deve usar os seguintes ingredientes: Sangue de águia, Veneno de cobra, use apenas esses ingredientes e nenhum outro, se necessário, de preferência use apenas os seguintes eletrodomésticos: Lata enferrujada"
    ## Testando a geração de receita pela IA

    receita_gerada = generate(prompt_proibida_2)
    receita_gerada_processada = ''
    for chunk in receita_gerada:
        receita_gerada_processada += chunk
    print(receita_gerada_processada)
    assert receita_gerada_processada ==""
