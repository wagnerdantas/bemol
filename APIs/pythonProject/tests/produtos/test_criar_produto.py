import requests

LOGIN_URL = "https://serverest.dev/login"
PRODUTOS_URL = "https://serverest.dev/produtos"


def obter_token():
    # Payload para login
    login_payload = {
        "email": "fulanosilva001@qa.com.br",
        "password": "teste"
    }

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    # Fazendo a requisição POST para obter o token
    response = requests.post(LOGIN_URL, json=login_payload, headers=headers)

    # Verificar se o login foi bem-sucedido
    if response.status_code != 200:
        print(f"Erro ao fazer login: Status {response.status_code}, Resposta: {response.text}")
        raise Exception(f"Erro ao fazer login: {response.status_code}")

    # Extraindo o token da resposta
    token = response.json().get('authorization')
    if not token:
        print("Token não encontrado na resposta de login.")
        raise Exception("Falha ao obter o token de autorização.")

    # Verificando o formato do token
    print(f"Token obtido com sucesso: {token}")
    if not token.startswith("Bearer "):
        token = f"Bearer {token}"

    return token


def criar_produto(token):
    # Payload para criar o produto
    produto_payload = {
        "nome": "Chocolate",
        "preco": 30,
        "descricao": "Cacau Show s1",
        "quantidade": 89
    }

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': token  # Usando o token diretamente
    }

    # Fazendo a requisição POST para criar o produto
    response = requests.post(PRODUTOS_URL, json=produto_payload, headers=headers)
    print(f"Tentativa de criação de produto. Status: {response.status_code}, Resposta: {response.text}")
    return response


def test_criar_produto():
    # Obter o token de autorização
    token = obter_token()

    # Tentar criar o produto
    response = criar_produto(token)

    # Se o token estiver expirado ou inválido, obter um novo token e tentar novamente
    if response.status_code == 401:
        print("Token expirado ou inválido. Obtendo novo token...")
        token = obter_token()
        response = criar_produto(token)

    # Imprimir o conteúdo da resposta para diagnóstico
    print(response.text)

    # Verificar se o status code é 201 (Created)
    assert response.status_code == 201, f"Esperado 201, mas recebeu {response.status_code}"


# Chamar a função para testar
test_criar_produto()
