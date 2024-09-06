import requests
from jsonschema import validate, ValidationError

LOGIN_URL = "https://serverest.dev/login"
PRODUTOS_URL = "https://serverest.dev/produtos"

# Schemas para validação
success_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "_id": {"type": "string"}
    },
    "required": ["message", "_id"]
}

error_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}

def obter_token():
    login_payload = {
        "email": "fulanosilva001@qa.com.br",
        "password": "teste"
    }

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    response = requests.post(LOGIN_URL, json=login_payload, headers=headers)

    if response.status_code != 200:
        print(f"Erro ao fazer login: Status {response.status_code}, Resposta: {response.text}")
        raise Exception(f"Erro ao fazer login: {response.status_code}")

    token = response.json().get('authorization')
    if not token:
        print("Token não encontrado na resposta de login.")
        raise Exception("Falha ao obter o token de autorização.")

    print(f"Token obtido com sucesso: {token}")
    if not token.startswith("Bearer "):
        token = f"Bearer {token}"

    return token

def criar_produto(token):
    produto_payload = {
        "nome": "waqa001",  # Altere o nome para algo único em cada execução
        "preco": 654,
        "descricao": "sasasas",
        "quantidade": 234
    }

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': token
    }

    response = requests.post(PRODUTOS_URL, json=produto_payload, headers=headers)
    print(f"Tentativa de criação de produto. Status: {response.status_code}, Resposta: {response.text}")
    return response

def test_criar_produto():
    token = obter_token()
    response = criar_produto(token)

    if response.status_code == 401:
        print("Token expirado ou inválido. Obtendo novo token...")
        token = obter_token()
        response = criar_produto(token)

    print(f"Resultado final: Status {response.status_code}, Resposta: {response.text}")

    # Validar o schema da resposta
    try:
        response_json = response.json()

        # Validar o schema com base no código de status
        if response.status_code == 201:
            validate(instance=response_json, schema=success_schema)
        elif response.status_code == 400:
            validate(instance=response_json, schema=error_schema)
        else:
            print(f"Resposta não esperada: Status {response.status_code}")
            assert False, "Resposta não esperada"

        print("Schema validado com sucesso.")
    except (ValidationError, ValueError) as e:
        print(f"Erro na validação do schema: {e}")
        assert False, "Resposta não corresponde ao schema esperado"

    assert response.status_code == 201, f"Esperado 201, mas recebeu {response.status_code}"

