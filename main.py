import argparse

from pynput.mouse import Listener as m_Listner
from pynput.keyboard import Listener as k_Listener
from services.listener import Listener
from services.simulator import Simulator
from utils.listeners import (
    KeyboardOnPress, KeyboardOnRelease, MouseOnClick
)

FUNCTIONS = {
    "simulator": "simulator",
    "listener": "listener"
}

parser = argparse.ArgumentParser()
parser.add_argument(
    "--func", type=str,
    help=f"{FUNCTIONS['simulator']} or {FUNCTIONS['listener']}"
)
args = parser.parse_args()


def main():
    if args.func == FUNCTIONS["simulator"]:
        Simulator.StartSimulate()
    elif args.func == FUNCTIONS["listener"]:
        Listener.StartListen()


if __name__ == "__main__":
    main()
