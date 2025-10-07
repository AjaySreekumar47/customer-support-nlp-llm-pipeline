from src.classifier import IntentClassifier
from src.summarizer import Summarizer
from src.reply_generator import ReplyGenerator

class SupportPipeline:
    def __init__(self, classifier_path="models/intent_classifier",
                 summarizer_path="models/summarizer",
                 reply_path="models/reply_generator",
                 label_names=None):
        self.classifier = IntentClassifier(classifier_path)
        self.summarizer = Summarizer(summarizer_path)
        self.replier = ReplyGenerator(reply_path)
        self.label_names = label_names

    def run(self, query):
        # Step 1: Intent classification
        intent, conf = self.classifier.predict(query, self.label_names)
        # Step 2: Summarization
        summary = self.summarizer.summarize(query)
        # Step 3: Reply generation
        reply = self.replier.generate(query, intent, summary)
        return {
            "query": query,
            "intent": intent,
            "confidence": conf,
            "summary": summary,
            "reply": reply
        }
