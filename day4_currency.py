import requests
response = requests.get("https://open.er-api.com/v6/latest/USD")
data = response.json()
print(data["rates"]["PKR"])