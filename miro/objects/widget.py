from miro.objects.base_miro_object import BaseMiroObject, MiroObjectType


class Widget(BaseMiroObject):

    def __init__(self, obj_id: str,
                 obj_type=MiroObjectType.WIDGET):
        super().__init__(obj_id, obj_type)
        self.obj_id = obj_id
        self.obj_type = obj_type

    def __repr__(self) -> str:
        return f'{self.obj_id}, {self.obj_type}'
