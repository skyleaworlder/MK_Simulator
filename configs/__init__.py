from pynput.keyboard import Key, KeyCode


FILE_APPENDER = "output.jg"

"""
About Mouse Listener
"""
MOUSE_LISTENER_LISTEN = ["MOUSE_ON_CLICK"]

MOUSE_LISTENER_END_X = 0
MOUSE_LISTENER_END_Y = 0

"""
About Keyboard Listener
"""
KEYBOARD_LISTENER_LISTEN = ["KEYBOARD_ON_PRESS", "KEYBOARD_ON_RELEASE"]
KEYBOARD_LISTENER_END_BUTTON: KeyCode = Key.esc
