import nltk
import re
from nltk.corpus import stopwords
from collections import Counter

class TextProcessor:
    def __init__(self):
        nltk.download('stopwords', quiet=True)
        self.stopwords = set(stopwords.words('english'))

    def tokenize_and_clean(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        return [word for word in words if word not in self.stopwords]
