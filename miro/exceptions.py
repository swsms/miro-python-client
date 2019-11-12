class MiroException(Exception):

    def __init__(self, status, details: str = ''):
        self.status = status
        self.details = details


class InvalidCredentialsException(MiroException):
    """An authentication error occurred because of bad credentials."""


class ObjectNotFoundException(MiroException):
    """The requested object was not found."""
