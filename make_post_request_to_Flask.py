import requests

url = 'http://localhost:{port}/wordcount'
data = {'url': 'https://www.example.com'}
response = requests.post(url, json=data)
print(response.json())