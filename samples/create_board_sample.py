from miro.client import MiroApiClient
from miro.utils import get_auth_token_from_env

client = MiroApiClient(base_url='https://api.miro.com',
                       auth_token=get_auth_token_from_env())

board = client.create_board('test-board', 'this is a test board')
print(board)
