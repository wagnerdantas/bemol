import requests

BASE_URL = "https://serverest.dev/usuarios"

def test_obter_usuarios_por_email():
    # Parâmetro de filtro: apenas o e-mail
    params = {
        'email': 'fulanosilva001@qa.com.br'
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

# Chamar a função para testar
test_obter_usuarios_por_email()
