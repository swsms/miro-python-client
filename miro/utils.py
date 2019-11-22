import os

from requests import Response

from miro.exceptions import *
from miro.objects.base_miro_object import MiroObjectType
from miro.objects.widgets import Line, Shape, Widget


def get_json_or_raise_exception(response: Response) -> dict:
    if is_2xx_status_code(response.status_code):
        return response.json()

    if response.status_code == 401:
        raise InvalidCredentialsException(response.status_code, response.text)

    if response.status_code == 403:
        raise InsufficientPermissions(response.status_code, response.text)

    if response.status_code == 404:
        raise ObjectNotFoundException(response.status_code, response.text)

    if is_5xx_status_code(response.status_code):
        raise MiroException(response.status_code, response.text)

    raise UnexpectedResponseException(response.status_code, response.text)


def is_2xx_status_code(status_code: int) -> bool:
    return str(status_code).startswith('2')


def is_5xx_status_code(status_code: int) -> bool:
    return str(status_code).startswith('5')


def get_auth_token_from_env() -> str:
    return os.environ.get('MIRO_AUTH_TOKEN', '')


def create_widget_by_type(widget_json) -> Widget:
    widget_type = widget_json['type']
    if widget_type == MiroObjectType.SHAPE:
        return Shape(obj_id=widget_json['id'],
                     text=widget_json['text'],
                     x_pos=widget_json['x'],
                     y_pos=widget_json['y'],
                     width=widget_json['width'],
                     height=widget_json['height'],
                     rotation=widget_json['rotation'])
    elif widget_type == MiroObjectType.LINE:
        return Line(obj_id=widget_json['id'],
                    start_widget_id=widget_json['startWidget']['id'],
                    end_widget_id=widget_json['endWidget']['id'])
    # TODO support texts
    return Widget(obj_id=widget_json['id'])
