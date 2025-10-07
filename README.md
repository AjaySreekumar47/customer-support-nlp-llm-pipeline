# Customer Support NLP/LLM Pipeline

A production-ready **end-to-end NLP pipeline** for customer support automation.  
This system integrates **intent classification, complaint summarization, and response generation** into a unified workflow.

---

## 📊 Architecture

```mermaid
flowchart LR
    A[User Query] --> B["Intent Classifier (DistilBERT)"]
    B -->|Predicted Intent| C["Summarizer (Flan-T5 LoRA)"]
    C -->|Condensed Summary| D["Reply Generator (Flan-T5 LoRA)"]
    D -->|Polite Reply| E[Final Output to Customer]
```

---

## 🚀 Features
- **Intent Classification** (DistilBERT fine-tuned on Banking77, ~89% acc/F1).
- **Summarization** (Flan-T5 + LoRA on CFPB consumer complaints).
- **Reply Generation** (Flan-T5 + LoRA on Twitter customer care data).
- Modular design with **src/** codebase (not just notebooks).
- Ready for **deployment & extension**.

---

## ⚙️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/customer-support-nlp-llm-pipeline.git
cd customer-support-nlp-llm-pipeline
pip install -r requirements.txt
````

---

## 🖥️ Usage

Run the full pipeline from the command line:

```bash
python main.py "My card hasn’t arrived yet, can I track delivery?"
```

Example output:

```
--- PIPELINE OUTPUT ---
Query: My card hasn’t arrived yet, can I track delivery?
Predicted Intent: card_arrival (confidence=0.72)
Summary: Customer has not received their card and wants to track delivery.
Reply: Hello, we'd love to help. Please DM us your details so we can check on your card delivery.
```

---

## 📂 Repository Structure

```
customer-support-nlp-llm-pipeline/
│
├── docs/                 # diagrams, evaluation metrics, documentation
├── models/               # model configs, adapters, registry.json
├── src/                  # pipeline modules
│   ├── classifier.py
│   ├── summarizer.py
│   ├── reply_generator.py
│   ├── pipeline.py
│   └── utils.py
├── main.py               # CLI entrypoint
├── requirements.txt      # full environment freeze
├── requirements_core.txt # lightweight install (essentials only)
└── README.md             # this file
```

---

## 📈 Models & Metrics

See [docs/evaluation.md](docs/evaluation.md) for detailed performance results.

* Intent Classifier: **Accuracy 88.9%**, Macro-F1 88.4%
* Summarizer: **ROUGE-L ~46.8**, strong compression
* Reply Generator: **BLEU ~10.6**, chrF ~30.8, ROUGE-L ~0.19

---

## 🛠️ Tools & Frameworks

* Python, PyTorch
* Hugging Face `transformers`, `datasets`, `evaluate`, `peft`
* sacreBLEU, scikit-learn
* Streamlit (dashboard)
* Colab Pro + A100/T4 GPUs

---

## 📜 License

MIT License.
