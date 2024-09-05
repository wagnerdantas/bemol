import requests

LOGIN_URL = "https://serverest.dev/login"
PRODUTOS_URL = "https://serverest.dev/produtos"


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
        "nome": "pdqfewfwef",  # Altere o nome para algo único em cada execução
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

    assert response.status_code == 201, f"Esperado 201, mas recebeu {response.status_code}"


#test_criar_produto()
