import requests
from jsonschema import validate, ValidationError

BASE_URL = "https://serverest.dev/usuarios"

# Definindo o schema para a resposta
response_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "_id": {"type": "string"}
    },
    "required": ["message", "_id"]
}

def test_criar_usuario():
    payload = {
        "nome": "Wagner",
        "email": "wagner@qa.com.br",
        "password": "teste",
        "administrador": "true"  # Ajustado para string conforme esperado pela API
    }

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    response = requests.post(BASE_URL, json=payload, headers=headers)

    # Imprimir o conteúdo da resposta para diagnóstico
    print(response.text)

    # Verificar se o status code é 201 (Created)
    assert response.status_code == 201, f"Esperado 201, mas recebeu {response.status_code}"

    # Validar o schema da resposta
    try:
        response_json = response.json()
        validate(instance=response_json, schema=response_schema)
        print("Schema validado com sucesso.")
    except (ValidationError, ValueError) as e:
        print(f"Erro na validação do schema: {e}")
        assert False, "Resposta não corresponde ao schema esperado"
