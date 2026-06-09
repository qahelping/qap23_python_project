import pytest
from faker import Faker

from core.http_client import HttpClient
from services.authentication_service import AuthenticationService
from services.boards_service import BoardsService
from services.users_service import UsersService


@pytest.mark.http_client1
def test_health_http_client():
    response = HttpClient().get('/health')

    assert response['status'] == 'ok'
    assert response['memory']


@pytest.mark.http_client1
def test_registration_user_http_client():
    fake = Faker()
    response = AuthenticationService().registration_user(fake.user_name(), fake.email(), "Qwerty123!")

    assert response['access_token']
    assert response['token_type'] == 'bearer'


@pytest.mark.http_client1
def test_get_user_info_http_client():
    fake = Faker()
    username, email = fake.user_name(), fake.email()

    response = AuthenticationService().registration_user(username, email, "Qwerty123!")

    assert response['access_token']
    assert response['token_type'] == 'bearer'

    headers = {
        'Authorization': f'Bearer {response['access_token']}',
        'accept': 'application/json'
    }

    response_users_me = HttpClient().get('/users/me', headers=headers)

    assert isinstance(response_users_me['id'], int)
    assert response_users_me["username"] == username
    assert response_users_me["email"] == email
    assert response_users_me['role'] == 'user'
    assert response_users_me['avatar_url'] is None
    assert response_users_me['created_at']


@pytest.mark.http_client1
def test_add_member_to_board():
    print('# ШAГ 1: admin token')
    admin_token = AuthenticationService().login('admin@example.com', 'admin123')

    print('# ШAГ 2: регистрация пользователя')
    new_user_token = AuthenticationService().registration_user(Faker().user_name(), Faker().email(),
                                                                           "Qwerty123!")

    print('# ШAГ 3: получение информации о пользователе')
    user_info_response = UsersService().get_user_me(new_user_token.access_token)

    print('# ШAГ 4: добавление нового пользователя на созданную доску')
    response = BoardsService().add_member_to_board(admin_token.access_token, board_id=1, user_id=user_info_response['id'])

    assert response['message'] == "User added to board"
