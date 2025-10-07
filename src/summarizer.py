from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class Summarizer:
    def __init__(self, model_path="models/summarizer"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path, device_map="auto")

    def summarize(self, text, max_len=80):
        inputs = self.tokenizer(
            "Summarize: " + text, return_tensors="pt", truncation=True, max_length=512
        ).to(self.model.device)
        output = self.model.generate(**inputs, max_length=max_len, num_beams=4)
        return self.tokenizer.decode(output[0], skip_special_tokens=True).strip()
