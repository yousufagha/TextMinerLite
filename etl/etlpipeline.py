from scraper import WebScraper
from textprocessor import TextProcessor

import pandas as pd
from collections import Counter

class ETLPipeline:
    def __init__(self, url):
        self.url = url

    def run(self):
        scraper = WebScraper(self.url)
        raw_text = scraper.extract_article_text()

        processor = TextProcessor()
        tokens = processor.tokenize_and_clean(raw_text)
        word_freq = Counter(tokens)

        df = pd.DataFrame(word_freq.items(), columns=['word', 'frequency'])
        df.sort_values(by='frequency', ascending=False, inplace=True)
        return df
