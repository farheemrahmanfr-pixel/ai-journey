import requests
city = input("Enter a city: ")
url = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name":city, "count": 1}
response = requests.get(url, params=params)
data = response.json()
place= data["results"][0]
print(place["name"], "-", place["country"])
print("latitude:", place["latitude"])
print("longitude:", place["longitude"])

weather_url= "https://api.open-meteo.com/v1/forecast"
weather_params= {
    "latitude": place["latitude"],
    "longitude": place["longitude"],
    "current": "temperature_2m",
}
weather = requests.get(weather_url, params=weather_params).json()
print("Temprature now:", weather["current"]["temperature_2m"], "\u00b0C")
