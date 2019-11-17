from miro.client import MiroApiClient
from miro.utils import get_auth_token_from_env

client = MiroApiClient(base_url='https://api.miro.com',
                       auth_token=get_auth_token_from_env())

widgets = client.get_all_widgets_by_board_id('o9J_kwX5tTk=')
for widget in widgets:
    print(widget)
