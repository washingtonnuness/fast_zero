from http import HTTPStatus
from conftest import client

# Função de test o que está sendo testado e o que precisa ser retornado caso ok
def test_read_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}

def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@mail.com',
            'password': 'password',
        },
    )
    #Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED

    #Validar UserPublic
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@mail.com',
    }

