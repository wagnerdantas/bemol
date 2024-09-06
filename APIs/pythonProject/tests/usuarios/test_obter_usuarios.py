import requests
from jsonschema import validate, ValidationError

BASE_URL = "https://serverest.dev/usuarios"

# Definindo o schema para a resposta
response_schema = {
    "type": "object",
    "properties": {
        "quantidade": {"type": "integer"},
        "usuarios": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string"},
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                    "administrador": {"type": "string"},
                    "_id": {"type": "string"}
                },
                "required": ["nome", "email", "password", "administrador", "_id"]
            }
        }
    },
    "required": ["quantidade", "usuarios"]
}

def test_obter_usuarios_por_email():
    # Parâmetro de filtro: apenas o e-mail
    params = {
        'email': 'wagner@qa.com.br'
    }

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    # Fazendo a requisição GET com o parâmetro de e-mail
    response = requests.get(BASE_URL, headers=headers, params=params)

    # Imprimir o conteúdo da resposta para diagnóstico
    print(response.text)

    # Verificar se o status code é 200 (OK)
    assert response.status_code == 200, f"Esperado 200, mas recebeu {response.status_code}"

    # Validar o schema da resposta
    try:
        response_json = response.json()
        validate(instance=response_json, schema=response_schema)
        print("Schema validado com sucesso.")
    except (ValidationError, ValueError) as e:
        print(f"Erro na validação do schema: {e}")
        assert False, "Resposta não corresponde ao schema esperado"
