from core.http_client import HttpClient


class BoardsService(HttpClient):
    SERVICE_URL = '/boards'

    def add_member_to_board(self, access_token, board_id, user_id):
        headers = {
            'Authorization': f'Bearer {access_token}',
            'accept': 'application/json'
        }

        return HttpClient().post(f'{self.SERVICE_URL}/{board_id}/members/{user_id}', headers=headers)
