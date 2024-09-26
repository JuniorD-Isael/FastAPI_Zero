from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_zero.app import app

client = TestClient(app)


def test_read_root_return_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert (verificação)
    assert response.json() == {'message': 'Olá, Mundo!'}  # Assert


def test_user():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/user')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert (vericicaça)
    assert response.json() == {'usuario': 'fulano'}  # Assert


def ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/ola-mundo')  # Act (ação)
    assert response.status_code == HTTPStatus.OK  # Assert (vericicaça)
    assert "<h1> Olá Mundo </h1>" in response.text
