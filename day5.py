import requests
response = requests.get("https://open.er-api.com/v6/latest/USD")
data = response.json()
while True:
    code = input("Enter a currency code (or type quit): ")
    code = code.upper()
    if code== "QUIT":
        break
    print("1 USD =", data["rates"][code], code)