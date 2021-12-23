from json import loads
import time

from pynput import keyboard, mouse
import configs
from models import BaseEvent
from models.mouse import MouseEvent, MousePressEvent, MouseReleaseEvent
from models.keyboard import KeyboardEvent, KeyboardPressEvent, KeyboardReleaseEvent
from utils.constructors import NewEvent
from utils.utils import SelectMouseButtonType


class Simulator:

    MOUSE_CTRL = mouse.Controller()
    KEYBOARD_CTRL = keyboard.Controller()

    @classmethod
    def StartSimulate(cls):
        with open(configs.FILE_APPENDER, "r") as f:
            time.sleep(1)
            while True:
                record = f.readline()
                if len(record) == 0:
                    break

                event = NewEvent(event=loads(record))
                if event.etype in [MousePressEvent.EVENT_TYPE, MouseReleaseEvent.EVENT_TYPE]:
                    event: MouseEvent = event
                    cls.MOUSE_CTRL.position = (event.coord.x, event.coord.y)
                    cls.MOUSE_CTRL.press(SelectMouseButtonType(event.button))
                elif event.etype == KeyboardPressEvent.EVENT_TYPE:
                    event: KeyboardPressEvent = event
                    cls.KEYBOARD_CTRL.press(keyboard.KeyCode.from_vk(event.key))
                elif event.etype == KeyboardReleaseEvent.EVENT_TYPE:
                    event: KeyboardReleaseEvent = event
                    cls.KEYBOARD_CTRL.release(keyboard.KeyCode.from_vk(event.key))

