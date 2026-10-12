import requests
try:
    response= requests.get("https://open.er-api.com/v6/latest/USD", timeout=10)
    data = response.json()
except requests.exceptions.RequestException:
    print("Could not get the exchange rates. Check your internet and try again.")
    exit()    
while True:
    code = input("Enter a currency code(or type quit): ").upper()
    if code=="QUIT":
        break
    try:
        print("1 USD=", data["rates"][code], code)
    except KeyError:
        print("Sorry,", code,"is not a valid currency code.")
print("Goodbye!")
                