import requests
url = "http://127.0.0.1:8000/weather/tokio/"
response = requests.get(url)
print(response.json())