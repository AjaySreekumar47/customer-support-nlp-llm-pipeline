import argparse
from src.pipeline import SupportPipeline
from src.utils import load_label_names

def main():
    parser = argparse.ArgumentParser(description="Customer Support NLP/LLM Pipeline")
    parser.add_argument("query", type=str, help="Customer query text")
    args = parser.parse_args()

    # Load label names (for intent classifier)
    try:
        label_names = load_label_names()
    except FileNotFoundError:
        label_names = None

    # Build pipeline
    pipeline = SupportPipeline(label_names=label_names)

    # Run
    result = pipeline.run(args.query)

    print("\n--- PIPELINE OUTPUT ---")
    print(f"Query: {result['query']}")
    print(f"Predicted Intent: {result['intent']} (confidence={result['confidence']:.3f})")
    print(f"Summary: {result['summary']}")
    print(f"Reply: {result['reply']}")

if __name__ == "__main__":
    main()
