import json

def load_label_names(path="models/intent_classifier/label_names.json"):
    with open(path) as f:
        return json.load(f)
