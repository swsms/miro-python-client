import requests

from miro.utils import get_json_or_raise_exception, UnexpectedResponseException
from miro.widget import Widget


class MiroApiClient:

    def __init__(self, base_url: str, auth_token: str):
        self.base_url = base_url
        self.auth_token = auth_token

    def get_all_widgets_by_board_id(self, board_id: str):
        headers = {'Authorization': f'Bearer {self.auth_token}'}

        url = f'{self.base_url}/v1/boards/{board_id}/widgets/'
        response = requests.get(url, headers=headers)
        collection_json = get_json_or_raise_exception(response)

        try:
            widgets_json = collection_json['data']
            return [Widget(object_id=w['id'],
                           object_type=w['type']) for w in widgets_json]
        except Exception as e:
            raise UnexpectedResponseException(cause=e)
