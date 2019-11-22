from miro.objects.base_miro_object import BaseMiroObject, MiroObjectType


class Board(BaseMiroObject):

    def __init__(self,
                 obj_id: str,
                 name: str,
                 description: str):
        super().__init__(obj_id, MiroObjectType.BOARD)
        self.name = name
        self.description = description
