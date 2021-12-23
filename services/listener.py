import configs

from pynput.mouse import Listener as MListner
from pynput.keyboard import Listener as KListener
from utils.listeners import KeyboardOnPress, KeyboardOnRelease, MouseOnClick

class Listener:

    LISTENER_MAP = {
        "KEYBOARD_ON_PRESS": KeyboardOnPress,
        "KEYBOARD_ON_RELEASE": KeyboardOnRelease,
        "MOUSE_ON_CLICK": MouseOnClick
    }

    @classmethod
    def StartListen(cls):
        all_lsn_used = configs.KEYBOARD_LISTENER_LISTEN + configs.MOUSE_LISTENER_LISTEN
        lsn_func_map = {
            lsn: cls.LISTENER_MAP[lsn] if lsn in all_lsn_used else None \
                for lsn in cls.LISTENER_MAP
        }
        with KListener(on_press=lsn_func_map["KEYBOARD_ON_PRESS"],
                       on_release=lsn_func_map["KEYBOARD_ON_RELEASE"]) as k_lsn, \
             MListner(on_click=lsn_func_map["MOUSE_ON_CLICK"]) as m_lsn:
            k_lsn.join()
            m_lsn.join()
