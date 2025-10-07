from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import torch

class IntentClassifier:
    def __init__(self, model_path="models/intent_classifier"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.pipe = TextClassificationPipeline(
            model=self.model,
            tokenizer=self.tokenizer,
            top_k=1,
            device=0 if torch.cuda.is_available() else -1
        )

    def predict(self, text, label_names=None):
        pred = self.pipe(text)[0][0]
        idx = int(pred["label"].split("_")[-1]) if "LABEL" in pred["label"] else int(pred["label"])
        intent = label_names[idx] if label_names else pred["label"]
        return intent, float(pred["score"])
