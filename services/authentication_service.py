import allure

from core.http_client import HttpClient
from models.token import TokenResponse


class AuthenticationService(HttpClient):
    SERVICE_URL  = '/auth'

    @allure.step("Registration user")
    def registration_user(self, username, email, password):
        body = {
            "username": username,
            "email": email,
            "password": password
        }

        return TokenResponse(**self.post(f'{self.SERVICE_URL}/register', body=body))

    @allure.step("Login user")
    def login(self, email, password):
        body = {
            "email": email,
            "password": password
        }

        return TokenResponse(**HttpClient().post(f'{self.SERVICE_URL}/login', body=body))
