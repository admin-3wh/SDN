from scn.inference import Inference
from scn.icm import InferenceChainMemory

def prompt_inference():
    subject = input("Enter subject: ").strip()
    predicate = input("Enter predicate: ").strip()
    value = input("Enter value: ").strip()
    confidence = float(input("Enter confidence (0.0 to 1.0): ").strip())
    source = input("Enter source (optional): ").strip() or "CLI Input"

    return Inference(
        subject=subject,
        predicate=predicate,
        value=value,
        confidence=confidence,
        source=source,
    )

def main():
    icm = InferenceChainMemory()
    print("🧠 Self-Contradiction Network (CLI)")
    print("Type 'exit' as subject to quit.\n")

    while True:
        inf = prompt_inference()
        if inf.subject.lower() == 'exit':
            break
        contradictions = icm.add_inference(inf)
        if contradictions:
            print("⚠️ Contradictions Detected:")
            for a, b in contradictions:
                print(f"  - {a.short()} ↔ {b.short()}")
        else:
            print("✅ No contradictions.")
        print("\nCurrent Beliefs:")
        print(icm)
        print("-" * 40)

if __name__ == "__main__":
    main()# CLI entry point for SCN
