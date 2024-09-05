import requests

BASE_URL = "https://serverest.dev/usuarios"


def test_criar_usuario():
    payload = {
        "nome": "Fulano da Silva",
        "email": "fulanosilva001@qa.com.br",
        "password": "teste",
        "administrador": "true"
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
