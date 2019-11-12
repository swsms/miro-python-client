class BaseObject:

    def __init__(self, object_id: str, object_type: str):
        self.object_id = object_id
        self.object_type = object_type


class Widget(BaseObject):

    def __repr__(self) -> str:
        return f'{self.object_id}, {self.object_type}'
