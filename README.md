# Customer Support NLP/LLM Pipeline

An end-to-end NLP pipeline for customer support automation. The project combines intent classification, complaint/query summarization, and response generation into a single command-line and Streamlit-ready workflow.

The pipeline uses local Hugging Face model artifacts stored under `models/` and a modular Python codebase under `src/`.

---

## Architecture

```mermaid
flowchart LR
    A[Customer Query] --> B["Intent Classifier<br/>DistilBERT"]
    B -->|Predicted Intent| C["Summarizer<br/>Flan-T5 + LoRA"]
    C -->|Condensed Summary| D["Reply Generator<br/>Flan-T5 + LoRA"]
    D -->|Support Reply| E[Final Output]
````

---

## Features

* Intent classification using a fine-tuned DistilBERT sequence classifier.
* Query/complaint summarization using a Flan-T5 LoRA adapter.
* Customer-support reply generation using a Flan-T5 LoRA adapter.
* Modular `src/` codebase with separate classifier, summarizer, reply generator, and pipeline modules.
* Command-line entry point through `main.py`.
* Streamlit app entry point through `app.py`.
* Included zipped model artifacts for reproducible local inference.
* Evaluation documentation under `docs/`.

---

## Repository Structure

```text
customer-support-nlp-llm-pipeline/
├── app.py
├── main.py
├── queries.csv
├── requirements.txt
├── README.md
├── docs/
│   ├── architecture.mmd
│   ├── evaluation.md
│   └── README.md
├── models/
│   ├── intent_classifier.zip
│   ├── summarizer.zip
│   ├── reply_generator.zip
│   └── README.md
└── src/
    ├── classifier.py
    ├── pipeline.py
    ├── reply_generator.py
    ├── summarizer.py
    ├── utils.py
    └── __init__.py
```

---

## Model Artifacts

The repository stores model artifacts as compressed zip files:

```text
models/
├── intent_classifier.zip
├── summarizer.zip
└── reply_generator.zip
```

Before running the pipeline locally, extract them into the `models/` directory.

Windows PowerShell:

```powershell
Expand-Archive models\intent_classifier.zip -DestinationPath models -Force
Expand-Archive models\summarizer.zip -DestinationPath models -Force
Expand-Archive models\reply_generator.zip -DestinationPath models -Force
```

After extraction, the expected structure is:

```text
models/
├── intent_classifier/
├── summarizer/
└── reply_generator/
```

The extracted model folders are local runtime artifacts and do not need to be committed.

---

## Setup

Python 3.10+ is recommended.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install runtime dependencies:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Extract the model artifacts:

```powershell
Expand-Archive models\intent_classifier.zip -DestinationPath models -Force
Expand-Archive models\summarizer.zip -DestinationPath models -Force
Expand-Archive models\reply_generator.zip -DestinationPath models -Force
```

---

## Command-Line Usage

Run the full pipeline from the command line:

```bash
python main.py "My card has not arrived yet. Can I track delivery?"
```

Example output from a local run:

```text
--- PIPELINE OUTPUT ---
Query: My card has not arrived yet. Can I track delivery?
Predicted Intent: LABEL_11 (confidence=0.716)
Summary: No, it's not yet. Can I track delivery?
Reply: USER> I'm sorry for the delay, we'd like to help you track your order. Please DM us your tracking number and a tracking number. SQ
```

Note: the released classifier artifact stores Hugging Face numeric labels such as `LABEL_0` through `LABEL_76`. A human-readable intent mapping can be added through:

```text
models/intent_classifier/label_names.json
```

if the original training label order is available.

---

## Streamlit Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app provides an interactive interface for testing the customer-support pipeline on example or user-provided queries.

---

## Models and Evaluation

See [`docs/evaluation.md`](docs/evaluation.md) for detailed performance notes.

Reported project metrics include:

| Component         | Model          | Reported Metric                       |
| ----------------- | -------------- | ------------------------------------- |
| Intent Classifier | DistilBERT     | Accuracy ~88.9%, Macro-F1 ~88.4%      |
| Summarizer        | Flan-T5 + LoRA | ROUGE-L ~46.8                         |
| Reply Generator   | Flan-T5 + LoRA | BLEU ~10.6, chrF ~30.8, ROUGE-L ~0.19 |

These metrics are from the original training/evaluation workflow and should be interpreted as project-level evaluation results rather than a deployed production benchmark.

---

## Code Overview

### `src/classifier.py`

Loads the local intent-classification model and predicts an intent label and confidence score.

### `src/summarizer.py`

Loads the summarization model/adapters and produces a condensed summary of the customer query.

### `src/reply_generator.py`

Generates a customer-support-style response using the original query, predicted intent, and summary.

### `src/pipeline.py`

Combines the classifier, summarizer, and reply generator into a single `SupportPipeline`.

### `main.py`

Provides the command-line entry point.

---

## Example Input Queries

The repository includes `queries.csv` with sample customer-support queries, such as:

```text
My card hasn’t arrived yet, can I track delivery?
Why was my cash withdrawal declined at the ATM?
How do I verify my identity to increase limits?
I was charged twice for my ticket booking, need refund.
```

---

## What This Project Demonstrates

This project demonstrates:

* transformer-based intent classification,
* seq2seq summarization,
* LoRA-adapted text generation,
* local Hugging Face model loading,
* modular NLP pipeline design,
* command-line inference,
* Streamlit interface development,
* evaluation documentation,
* packaging model artifacts for reproducible portfolio demos.

---

## Known Limitations

* The classifier artifact currently exposes generic Hugging Face labels (`LABEL_0` … `LABEL_76`) unless a separate `label_names.json` mapping is provided.
* The summarizer and reply generator are local model/adaptor artifacts and may produce imperfect or repetitive phrasing.
* The project is intended as a portfolio/research pipeline, not a production customer-support system.
* The model zip files must be extracted before running local inference.
* GPU acceleration is optional; CPU inference works but may be slower.

---

## License

MIT License.