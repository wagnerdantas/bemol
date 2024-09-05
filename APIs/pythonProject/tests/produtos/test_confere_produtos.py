import requests

product_id: str = "EJO623YoXcgJkvGH"

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

    # Conteúdo esperado no corpo da resposta (ajuste conforme necessário)
    expected_response = {
        "nome": "Chocolate",
        "preco": 30,
        "descricao": "Cacau Show s1",
        "quantidade": 89,
        "_id": product_id
    }

    # Converte a resposta para JSON
    response_json = response.json()

    # Verifica se a resposta corresponde ao esperado
    assert response_json == expected_response, f"Resposta esperada: {expected_response}, mas recebeu: {response_json}"
