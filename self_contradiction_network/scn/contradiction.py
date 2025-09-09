# Contradiction detection logic
from scn.inference import Inference

def contradicts(a: Inference, b: Inference) -> bool:
    # Basic contradiction: same subject + predicate, different value
    return (
        a.subject == b.subject and
        a.predicate == b.predicate and
        a.value != b.value
    )
