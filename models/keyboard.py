from typing import Dict, Union

from pynput import keyboard
from . import BaseEvent

class KeyboardEvent(BaseEvent):

    EVENT_TYPE = "Keyboard"

    def __init__(self,
                 key: keyboard.KeyCode,
                 comment: str) -> None:
        super().__init__(comment)
        self.key = key

    def serialize(self) -> Dict:
        return super().serialize()


class KeyboardPressEvent(KeyboardEvent):
    EVENT_TYPE = "KeyboardPress"


class KeyboardReleaseEvent(KeyboardEvent):
    EVENT_TYPE = "KeyboardRelease"
