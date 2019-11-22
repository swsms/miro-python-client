from miro.objects.base_miro_object import BaseMiroObject, MiroObjectType


class Widget(BaseMiroObject):

    def __init__(self, obj_id: str,
                 obj_type=MiroObjectType.WIDGET):
        super().__init__(obj_id, obj_type)
        self.obj_id = obj_id
        self.obj_type = obj_type
        self.capabilities = dict()
        self.metadata = dict()


class Shape(Widget):

    def __init__(self, obj_id: str, text: str,
                 x_pos: float, y_pos: float,
                 width: float, height: float,
                 rotation: float):
        super().__init__(obj_id, MiroObjectType.SHAPE)
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.rotation = rotation  # number of degrees clockwise


class Line(Widget):

    def __init__(self, obj_id: str,
                 start_widget_id: str,
                 end_widget_id: str):
        super().__init__(obj_id, MiroObjectType.LINE)
        self.start_widget_id = start_widget_id
        self.end_widget_id = end_widget_id
