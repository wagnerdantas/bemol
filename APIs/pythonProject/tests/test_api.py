import requests


def test_api_status_code():
    response = requests.post("http://localhost", timeout=10)
    assert response.status_code == 200
