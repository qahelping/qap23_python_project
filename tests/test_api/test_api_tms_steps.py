import pytest
from faker import Faker

from core.http_client import HttpClient
from services.authentication_service import AuthenticationService
from services.boards_service import BoardsService
from services.users_service import UsersService
from steps.board_steps import add_new_member_to_step_by_admin


@pytest.mark.steps
def test_add_member_to_board_steps():
    response = add_new_member_to_step_by_admin()
    assert response['message'] == "User added to board"
