from typing import List

import requests

from miro.board import Board
from miro.utils import get_json_or_raise_exception, UnexpectedResponseException
from miro.widget import Widget


class MiroApiClient:

    def __init__(self, base_url: str, auth_token: str):
        self.base_url = base_url
        self.auth_token = auth_token
        self.auth_header_as_dict = {
            'Authorization': f'Bearer {self.auth_token}'
        }

    def get_all_widgets_by_board_id(self, board_id: str) -> List[Widget]:
        url = f'{self.base_url}/v1/boards/{board_id}/widgets/'
        response = requests.get(url, headers=self.auth_header_as_dict)
        collection_json = get_json_or_raise_exception(response)

        try:
            widgets_json = collection_json['data']
            return [Widget(object_id=w['id'],
                           object_type=w['type']) for w in widgets_json]
        except Exception as e:
            raise UnexpectedResponseException(cause=e)

    def get_board_by_id(self, board_id: str) -> Board:
        url = f'{self.base_url}/v1/boards/{board_id}'
        response = requests.get(url, headers=self.auth_header_as_dict)
        board_json = get_json_or_raise_exception(response)

        try:
            return Board(
                object_id=board_json['id'],
                object_type=board_json['type'],
                name=board_json['name'],
                description=board_json['description']
            )
        except Exception as e:
            raise UnexpectedResponseException(cause=e)

    def create_board(self, name: str, description: str) -> Board:
        headers = {
            'Content-Type': 'application/json'
        }
        headers.update(self.auth_header_as_dict)

        board_data = {
            'name': name,
            'description': description
        }

        url = f'{self.base_url}/v1/boards'
        response = requests.post(url, json=board_data, headers=headers)

        board_json = get_json_or_raise_exception(response)

        try:
            return Board(
                object_id=board_json['id'],
                object_type=board_json['type'],
                name=board_json['name'],
                description=board_json['description']
            )
        except Exception as e:
            raise UnexpectedResponseException(cause=e)
