class MiroException(Exception):

    def __init__(self, status: int, details: str = ''):
        self.status = status
        self.details = details

    def __init__(self, cause: Exception):
        super(MiroException, self).__init__(cause)


class InvalidCredentialsException(MiroException):
    """An authentication error occurred because of bad credentials."""


class ObjectNotFoundException(MiroException):
    """The requested object was not found."""


class UnexpectedResponseException(MiroException):
    """The response has an unexpected code or data"""


class InsufficientPermissions(MiroException):
    """Not enough permissions to perform a certain action"""
