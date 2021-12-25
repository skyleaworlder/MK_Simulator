from typing import Dict
from models import BaseEvent
from models.mouse import MouseEvent, MousePressEvent, MouseReleaseEvent
from models.keyboard import KeyboardEvent, KeyboardPressEvent, KeyboardReleaseEvent


def NewMouseEvent(id, time, x, y, button, press=True) -> MouseEvent:
    coord = MouseEvent.MouseCoord(x, y)
    if press:
        return MousePressEvent(id=id, time=time, button=button, comment="", coord=coord)
    return MouseReleaseEvent(id=id, time=time, button=button, comment="", coord=coord)


def NewKeyboardEvent(id, time, key, press=True) -> KeyboardEvent:
    if press:
        return KeyboardPressEvent(id=id, time=time, key=key, comment="")
    return KeyboardReleaseEvent(id=id, time=time, key=key, comment="")


def NewEvent(event: Dict) -> BaseEvent:
    if event["type"] in [MousePressEvent.EVENT_TYPE, MouseReleaseEvent.EVENT_TYPE]:
        return NewMouseEvent(id=event["id"], time=event["time"],
                                x=event["coord"]["x"], y=event["coord"]["y"],
                                button=event["button"], press=(event["type"] == MousePressEvent.EVENT_TYPE))
    elif event["type"] in [KeyboardPressEvent.EVENT_TYPE, KeyboardReleaseEvent.EVENT_TYPE]:
        return NewKeyboardEvent(id=event["id"], time=event["time"],
                                key=event["key"], press=(event["type"] == KeyboardPressEvent.EVENT_TYPE))

