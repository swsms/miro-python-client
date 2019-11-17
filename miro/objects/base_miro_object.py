from enum import Enum


class MiroObjectType(Enum):
    BOARD = 'board'
    WIDGET = 'widget'
    USER_MINI = 'user'
    SHAPE = 'shape'
    LINE = 'line'
    TEXT = 'text'


class BaseMiroObject:
    def __init__(self, obj_id: str,
                 obj_type: MiroObjectType):
        self.obj_id = obj_id
        self.obj_type = obj_type
