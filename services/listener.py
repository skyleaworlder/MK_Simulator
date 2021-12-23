import configs

from pynput.mouse import Listener as MListner
from pynput.keyboard import Listener as KListener
from utils.listeners import LISTENER_MAP

class Listener:
    @classmethod
    def StartListen(cls):
        all_lsn_used = configs.KEYBOARD_LISTENER_LISTEN + configs.MOUSE_LISTENER_LISTEN
        lsn_func_map = {
            lsn: LISTENER_MAP[lsn] if lsn in all_lsn_used else None \
                for lsn in LISTENER_MAP
        }
        with KListener(on_press=lsn_func_map["KEYBOARD_ON_PRESS"],
                        on_release=lsn_func_map["KEYBOARD_ON_RELEASE"]) as k_lsn, \
             MListner(on_click=lsn_func_map["MOUSE_ON_CLICK"]) as m_lsn:
            k_lsn.join()
            m_lsn.join()
