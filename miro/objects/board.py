from miro.objects.base_miro_object import BaseMiroObject, MiroObjectType


class Board(BaseMiroObject):

    def __init__(self,
                 obj_id: str,
                 name: str,
                 description: str):
        super().__init__(obj_id, MiroObjectType.BOARD)
        self.name = name
        self.description = description
        self.capabilities = dict()
        self.metadata = dict()

    def __repr__(self) -> str:
        return f'{self.obj_id}, {self.obj_type}, {self.name}, {self.description}'
