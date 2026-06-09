from services.authentication_service import AuthenticationService


def registration_user(user_name, email):
    response = AuthenticationService().registration_user(user_name, email, "Qwerty123!")

    return response.access_token
