from core.http_client import HttpClient
from models.user import UserResponse


class UsersService(HttpClient):
    SERVICE_URL  = '/users'

    def get_user_me(self, access_token) -> UserResponse:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'accept': 'application/json'
        }
        user_response = self.get(f'{self.SERVICE_URL}/me', headers=headers)
        return UserResponse(**user_response)


