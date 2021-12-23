from typing import Dict, Tuple

from pynput.keyboard import Key
import configs
from models.mouse import MouseEvent, MousePressEvent, MouseReleaseEvent
from models.keyboard import KeyboardEvent, KeyboardPressEvent, KeyboardReleaseEvent
from time import time_ns
from utils.constructors import NewKeyboardEvent, NewMouseEvent
from utils.utils import GetID
from utils.wrappers import for_listener, log_output


@for_listener
@log_output
def MouseOnClick(x, y, button, press) -> Tuple[bool, Dict]:
    event: MouseEvent = NewMouseEvent(GetID(), time_ns(), x, y, button, press)
    go_on: bool = True
    if x == configs.MOUSE_LISTENER_END_X or y == configs.MOUSE_LISTENER_END_Y:
        go_on = False
    return go_on, event.serialize()


def KeyboardOnClick(key, press) -> Tuple[bool, Dict]:
    event: KeyboardEvent = NewKeyboardEvent(GetID(), time_ns(), key, press)
    go_on: bool = True
    if event.key == configs.KEYBOARD_LISTENER_END_BUTTON:
        go_on = False
    return go_on, event.serialize()


@for_listener
@log_output
def KeyboardOnPress(key) -> Tuple[bool, Dict]:
    return KeyboardOnClick(key, press=True)


@for_listener
@log_output
def KeyboardOnRelease(key) -> Tuple[bool, Dict]:
    return KeyboardOnClick(key, press=False)
