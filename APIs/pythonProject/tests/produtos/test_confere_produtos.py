import pytest
import requests
from jsonschema import validate, ValidationError

# Definindo o schema para a resposta
response_schema = {
    "type": "object",
    "properties": {
        "nome": {"type": "string"},
        "preco": {"type": "integer"},
        "descricao": {"type": "string"},
        "quantidade": {"type": "integer"},
        "_id": {"type": "string"}
    },
    "required": ["nome", "preco", "descricao", "quantidade", "_id"]
}

@pytest.fixture
def product_id():
    return "WJUprA7Zgh2eoKiU"  # Defina o valor do ID aqui

def test_get_produto(product_id):
    # URL base da requisição
    url = f"https://serverest.dev/produtos/{product_id}"

    # Cabeçalhos da requisição
    headers = {
        'accept': 'application/json'
    }

    # Realiza a chamada GET
    response = requests.get(url, headers=headers)

    # Verifica se o status code é 200 (OK)
    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"

    # Converte a resposta para JSON
    response_json = response.json()

    # Validar o schema da resposta
    try:
        validate(instance=response_json, schema=response_schema)
        print("Schema validado com sucesso.")
    except ValidationError as e:
        print(f"Erro na validação do schema: {e}")
        assert False, "Resposta não corresponde ao schema esperado"

    # Conteúdo esperado no corpo da resposta (ajuste conforme necessário)
    expected_response = {
        "nome": "waqa001",
        "preco": 654,
        "descricao": "sasasas",
        "quantidade": 234,
        "_id": product_id
    }

    # Verifica se a resposta corresponde ao esperado
    assert response_json == expected_response, f"Resposta esperada: {expected_response}, mas recebeu: {response_json}"
