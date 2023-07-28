import requests
import json as js

city = input("Enter the city name:\n ").lower()

url = "https://api.weatherapi.com/v1/current.json?key=3286a549d0d744d0a4c191214232807&q={city}}"

r = requests.get(url)
print(r.text)

wdic=js.loads(r.text)

print( wdic["current"]["temp_c"])

