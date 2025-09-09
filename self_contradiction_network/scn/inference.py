from dataclasses import dataclass, field
from typing import Any, List, Optional
import time
import uuid

@dataclass
class Inference:
    subject: str                  # The entity being described (e.g., "bird")
    predicate: str                # The attribute or relation (e.g., "color")
    value: Any                    # The value asserted (e.g., "blue")
    confidence: float = 1.0       # Confidence score [0.0 - 1.0]
    source: Optional[str] = None  # Origin of the inference (e.g., user input, model)
    timestamp: float = field(default_factory=time.time)  # When the inference was made
    trace: Optional[List[str]] = field(default_factory=list)  # Reasoning path
    id: str = field(default_factory=lambda: str(uuid.uuid4()))  # Unique ID

    def __str__(self):
        return (f"Inference({self.subject}.{self.predicate} = {self.value}, "
                f"conf={self.confidence}, time={self.timestamp}, id={self.id})")

    def short(self):
        return f"{self.subject}.{self.predicate} = {self.value}"# Inference class and data structure
