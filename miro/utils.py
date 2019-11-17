import os

from requests import Response

from miro.exceptions import *


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
