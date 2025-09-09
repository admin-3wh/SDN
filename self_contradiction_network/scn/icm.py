from typing import List
from scn.inference import Inference
from scn.contradiction import contradicts

class InferenceChainMemory:
    def __init__(self):
        self.memory: List[Inference] = []

    def add_inference(self, new_inf: Inference) -> List[tuple]:
        """Add a new inference to memory, return list of contradictions if any."""
        contradictions = []
        for existing in self.memory:
            if contradicts(existing, new_inf):
                contradictions.append((existing, new_inf))
        self.memory.append(new_inf)
        return contradictions

    def get_beliefs(self) -> List[Inference]:
        """Return the current list of inferences."""
        return self.memory

    def __str__(self):
        return "\n".join(inf.short() for inf in self.memory)# Inference Chain Memory (ICM) logic
