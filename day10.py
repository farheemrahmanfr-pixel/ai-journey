import os
import requests
from dotenv import load_dotenv
api_key = os.getenv ("OPENWEATHER_API_KEY")
city = input("Enter a city: ")
url = "https://openweathermap.org/data/2.5/weather"
params = {"q":city,"appid": api_key, "units": "metric" }
response = requests.get(url, params=params)
print(response.status_code)
data = response.json()
print(data["main"]["temp"], "\u00b0C")
print(data["weather"][0]["description"])
