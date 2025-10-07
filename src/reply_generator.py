from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class ReplyGenerator:
    def __init__(self, model_path="models/reply_generator"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path, device_map="auto")

    def generate(self, query, intent, summary, max_len=80):
        prompt = f"Query: {query}\nIntent: {intent}\nSummary: {summary}\nReply:"
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=256).to(self.model.device)
        output = self.model.generate(**inputs, max_length=max_len, do_sample=True, top_p=0.9, temperature=0.7)
        return self.tokenizer.decode(output[0], skip_special_tokens=True).strip()
