import requests
response = requests.get("https://open.er-api.com/v6/latest/USD")
print(response.status_code)
print(response.text)
