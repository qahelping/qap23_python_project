import json

import requests

from core.log_base import logger


class HttpClient:
    DOMAIN = 'http://localhost:8000'

    def make_request(self, method, url, body: dict | None = None, headers: dict | None = None ):
        response = requests.request(method, self.DOMAIN + url, data=json.dumps(body), headers=headers)

        try:
            response.raise_for_status()
            response_json = response.json()
            logger.info(f'{response.url}:: {response_json}')

            return response_json
        except requests.exceptions.HTTPError as err:
            logger.error(f'Ошибка HTTP: {err}')

            assert False, f'Ошибка HTTP: {err}'


    def get(self, url, headers: dict | None = None):
        return self.make_request('GET', url, headers=headers)

    def post(self, url, body: dict | None = None, headers: dict | None = None):
        return self.make_request('POST', url, body=body, headers=headers)

