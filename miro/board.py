from miro.widget import BaseObject


class Board(BaseObject):

    def __init__(self,
                 object_id: str,
                 object_type: str,
                 name: str,
                 description: str):
        super(Board, self).__init__(object_id, object_type)
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f'{self.object_id}, {self.object_type}, {self.name}, {self.description}'
