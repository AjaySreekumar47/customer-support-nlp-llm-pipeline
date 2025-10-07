# 🤖 Models Directory

_Last updated: 2025-10-07 18:31:25 UTC_

This folder contains trained model artifacts for each stage of the Customer Support NLP Pipeline:

## Intent Classifier (DistilBERT – Banking77)
- **Description:** Fine-tuned DistilBERT model for intent recognition on 77 banking categories.
- **Dataset:** Banking77
- **Key Metrics:** Accuracy: 0.889 | F1: 0.884
- **Included Files:**
  - `accuracy`
  - `dataset`
  - `macro_f1`
  - `model`
  - `path`

## Reply Generator (Flan-T5 + LoRA)
- **Description:** Instruction-tuned adapter generating polite customer support replies from summarized context.
- **Dataset:** Twitter Customer Care
- **Key Metrics:** BLEU ≈ 3.4 | chrF ≈ 29.1 | ROUGE-L ≈ 0.19
- **Included Files:**
  - `bleu`
  - `chrf`
  - `dataset`
  - `model`
  - `path`
  - `rougeL`

## Complaint Summarizer (Flan-T5 + LoRA)
- **Description:** Summarization adapter trained on CFPB consumer complaints (tax & credit topics).
- **Dataset:** CFPB Complaints
- **Key Metrics:** ROUGE-L ≈ 0.46 | Compression ≈ 0.12
- **Included Files:**
  - `dataset`
  - `model`
  - `path`
  - `rougeL`

## 📘 registry.json
The `registry.json` file lists tracked model components and their files for reproducible loading.

> ⚠️ **Large weights (.bin / .safetensors)** are managed via Git LFS. Run `git lfs pull` after cloning.
