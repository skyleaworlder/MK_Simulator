from time import time_ns
from typing import Dict
from uuid import UUID, uuid4

class BaseEvent:

    EVENT_TYPE = "Base"

    def __init__(self, id: str, time: int, comment: str) -> None:
        self.id: str = id
        self.etype: str = self.EVENT_TYPE
        self.time: int = time
        self.comment: str = comment or ""

    def serialize(self) -> Dict:
        return {
            "id": self.id, "type": self.etype,
            "time": self.time, "comment": self.comment
        }
