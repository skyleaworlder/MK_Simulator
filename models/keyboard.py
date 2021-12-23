from typing import Dict, Union

from pynput import keyboard
from . import BaseEvent

class KeyboardEvent(BaseEvent):

    EVENT_TYPE = "Keyboard"

    def __init__(self,
                 id: str,
                 time: int,
                 key: keyboard.KeyCode,
                 comment: str) -> None:
        super().__init__(id, time, comment)
        self.key = key

    def serialize(self) -> Dict:
        res = super().serialize()
        print(self.key.__dict__)
        if hasattr(self.key, "vk"):
            res.update({"key": self.key.vk})
        elif hasattr(self.key, "_value_"):
            res.update({"key": self.key._value_.vk})
        return res


class KeyboardPressEvent(KeyboardEvent):
    EVENT_TYPE = "KeyboardPress"


class KeyboardReleaseEvent(KeyboardEvent):
    EVENT_TYPE = "KeyboardRelease"
