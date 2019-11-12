from miro.client import MiroApiClient

client = MiroApiClient(base_url='https://api.miro.com/',
                       auth_token='your-token')

json_widgets = client.get_all_widgets_by_board_id('board-id')
print(json_widgets)
