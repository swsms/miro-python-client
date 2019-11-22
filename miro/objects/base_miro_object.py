import json
from enum import Enum


class MiroObjectType(str, Enum):
    BOARD = 'board'
    WIDGET = 'widget'
    USER_MINI = 'user'
    SHAPE = 'shape'
    LINE = 'line'
    TEXT = 'text'

    def __repr__(self) -> str:
        return self.value


class JsonSerializableMixin:

    def __repr__(self) -> str:
        return json.dumps(self.__dict__)


class BaseMiroObject(JsonSerializableMixin):
    def __init__(self, obj_id: str,
                 obj_type: MiroObjectType):
        self.obj_id = obj_id
        self.obj_type = obj_type
