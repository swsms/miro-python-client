from miro.client import MiroApiClient

client = MiroApiClient(base_url='https://api.miro.com',
                       auth_token='your_token')

widgets = client.get_all_widgets_by_board_id('o9J_kwWZOu0=')
for widget in widgets:
    print(widget)
