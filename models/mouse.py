from typing import Dict

from pynput import mouse
from . import BaseEvent

class MouseEvent(BaseEvent):
    """ MouseEvent 是用来存储鼠标事件属性的 """

    class MouseCoord:
        def __init__(self, x: int, y: int) -> None:
            self.x: int = x
            self.y: int = y

        def serialize(self) -> Dict:
            return {"x": self.x, "y": self.y}

    EVENT_TYPE = "Mouse"

    def __init__(self,
                 button: mouse.Button,
                 comment: str,
                 coord: MouseCoord) -> None:
        super().__init__(comment)
        self.button = button
        self.coord = coord

    def serialize(self) -> Dict:
        res = super().serialize()
        res.update({"coord": self.coord.serialize()})
        return res


class MousePressEvent(MouseEvent):
    EVENT_TYPE = "MousePress"


class MouseReleaseEvent(MouseEvent):
    EVENT_TYPE = "MouseRelease"
