from pynput.mouse import Button
from uuid import uuid4


def SelectMouseButtonType(t: str) -> Button:
    if t == "left":
        return Button.left
    elif t == "middle":
        return Button.middle
    elif t == "right":
        return Button.right
    elif t == "x1":
        return Button.x1
    elif t == "x2":
        return Button.x2
    elif t == "unknown":
        return Button.unknown


def GetID() -> str:
    return str(uuid4())[-6:]
