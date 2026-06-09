from faker import Faker

from services.authentication_service import AuthenticationService
from services.boards_service import BoardsService
from services.users_service import UsersService
from steps.regitration_step import registration_user


def add_new_member_to_step_by_admin():
    auth_service = AuthenticationService()
    admin_token = auth_service.login('admin@example.com', 'admin123')

    new_user_token = registration_user(Faker().user_name(), Faker().email(), "Qwerty123!")
    user_info = UsersService().get_user_me(new_user_token)

    return BoardsService().add_member_to_board(admin_token.access_token, board_id=1, user_id=user_info.id)
