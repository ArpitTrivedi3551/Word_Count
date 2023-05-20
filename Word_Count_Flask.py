import requests
from bs4 import BeautifulSoup
from collections import Counter
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/wordcount', methods=['POST'])
def wordcount():
    url = request.json['url']
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()
    words = text.split()
    word_count = Counter(words)
    return jsonify(word_count)

if __name__ == '__main__':
    app.run()
