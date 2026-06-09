import json

import pytest
import requests
from faker import Faker

from core.http_client import HttpClient


@pytest.mark.api1
def test_health_check():
    response = requests.get('http://localhost:8000/health')
    assert response.status_code == 200

    response_json = response.json()
    assert response_json['status'] == 'ok'
    assert response_json['memory'] == {'used_mb': 80.4, 'percent': 11.6}


@pytest.mark.api2
def test_health_check_raise_for_status():
    response = requests.get('http://localhost:8000/health1')

    try:
        response.raise_for_status()
        response_json = response.json()
        assert response_json['status'] == 'ok'
        assert response_json['memory']

        print("Запрос успешен.")
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")
        assert False


@pytest.mark.api3
def test_health_optimize():
    response = HttpClient().get('/health')

    assert response['status'] == 'ok'
    assert response['memory']


@pytest.mark.api4
def test_registration_user_post():
    """
    curl -X 'POST' \
      'http://localhost:8000/auth/register' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "username": "user@example.com",
      "email": "user@example.com",
      "password": "Qwerty123!"
    }'

    """
    fake = Faker()
    body = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": "Qwerty123!"
    }

    print(body)

    response = requests.post('http://localhost:8000/auth/register', data=json.dumps(body))
    response_json = response.json()
    breakpoint()

    assert response.status_code == 201
    assert response_json['access_token']
    assert response_json['token_type'] == 'bearer'


@pytest.mark.api5
def test_get_user_info():
    fake = Faker()
    body = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": "Qwerty123!"
    }

    print('>>> user_body:', body)

    response = requests.post('http://localhost:8000/auth/register', data=json.dumps(body))
    response_json = response.json()
    assert response.status_code == 201

    access_token = response_json['access_token']

    print(">>> access_token:", access_token)
    breakpoint()

    """
    curl -X 'GET' \
        'http://localhost:8000/users/me' \
        -H 'accept: application/json' \
        -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....'
    """

    headers = {
        'Authorization': f'Bearer {access_token}',
        'accept': 'application/json'
    }

    response = requests.get('http://localhost:8000/users/me', headers=headers)
    response_json = response.json()
    print(">>> response_json:", response_json)
    breakpoint()

    assert response.status_code == 200

    assert isinstance(response_json['id'], int)
    assert response_json["username"] == body["username"]
    assert response_json["email"] == body["email"]
    assert response_json['role'] == 'user'
    assert response_json['avatar_url'] is None
    assert response_json['created_at']
