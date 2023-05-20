import requests
from bs4 import BeautifulSoup
from collections import Counter

class WordCounter:

    def __init__(self, url):
        self.url = url

    def get_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_text(self):
        html = self.get_html()
        if html:
            soup = BeautifulSoup(html, "html.parser")
            text = soup.get_text()
            return text
        else:
            return None

    def get_word_count(self):
        text = self.get_text()
        if text:
            words = text.lower().split()
            counter = Counter(words)
            return counter
        else:
            return None

    def get_json(self):
        word_count = self.get_word_count()
        if word_count:
            json_data = dict(word_count)
            return json_data
        else:
            return None

if __name__ == "__main__":
    site_url = input("Pleas enter the url:")
    word_counter = WordCounter(site_url)
    output = word_counter.get_json()
    print(output)
