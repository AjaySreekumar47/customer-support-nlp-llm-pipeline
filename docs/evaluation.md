# Evaluation Results

## Intent Classifier
- Accuracy: ~88.9%
- Macro F1: ~0.884
- Common confusion: card_arrival vs card_linking

## Summarizer
- ROUGE-L: ~46
- Compression ratio: ~0.12

## Reply Generator
- BLEU: ~10.6 | chrF: ~30.8 | ROUGE-L: ~0.19
- Produces polite, context-aware replies

## End-to-End Example
Query: "My card hasn’t arrived yet, can I track delivery?"
- Intent: card_arrival
- Summary: Customer reports card not yet delivered
- Reply: "We’re sorry to hear about the delay! Please DM us your order ID so we can check the status."
