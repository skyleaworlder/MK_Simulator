from models.mouse import MouseEvent, MousePressEvent, MouseReleaseEvent
from models.keyboard import KeyboardEvent, KeyboardPressEvent, KeyboardReleaseEvent


def NewMouseEvent(x, y, button, press=True) -> MouseEvent:
    coord = MouseEvent.MouseCoord(x, y)
    if press:
        return MousePressEvent(button=button, comment="", coord=coord)
    return MouseReleaseEvent(button=button, comment="", coord=coord)


def NewKeyboardEvent(key, press=True) -> KeyboardEvent:
    if press:
        return KeyboardPressEvent(key=key, comment="")
    return KeyboardReleaseEvent(key=key, comment="")
