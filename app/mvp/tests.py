from routes import generate_message, generate

def test_generating_prompt():
    ## Testando a geração de prompt
    contexto_seguro = {}
    contexto_proibido = {}
    assert generate_message()=={}


def test_generating_recipe():
    ## Testando a geração de receita pela IA
    assert generate("")!="" ## Se passar é por que foi gerado algo