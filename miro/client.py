import requests


class MiroApiClient:

    def __init__(self, base_url: str, auth_token: str):
        self.base_url = base_url
        self.auth_token = auth_token

    def get_all_widgets_by_board_id(self, board_id: str):
        headers = {'Authorization': f'Bearer {self.auth_token}'}

        url = f'{self.base_url}/v1/boards/{board_id}/widgets/'
        r = requests.get(url, headers=headers)
        return r.json()
