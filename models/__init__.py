from time import time_ns
from typing import Dict
from uuid import UUID, uuid4

class BaseEvent:

    EVENT_TYPE = "Base"

    def __init__(self, comment: str) -> None:
        self.id: str = str(uuid4())[-6:]
        self.etype: str = self.EVENT_TYPE
        self.time: int = time_ns()
        self.comment: str = comment or ""

    def serialize(self) -> Dict:
        return {
            "id": self.id, "type": self.etype,
            "time": self.time, "comment": self.comment
        }
