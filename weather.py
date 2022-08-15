# getting weather information by using openweatherAPI and python

import requests

API_Key = "372d6cb76200cd6b5d6c27c30f84c1ee"  # taking this key from https://home.openweathermap.org/api_keys

city = input("Enter a city: "

base_url = f"http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}"  # building url to make get request for user's input city

weather_data = requests.get(base_url).json()  # converting data to json format to have subscriptable object

print(round(weather_data["main"]["temp"] - 273.15), "° C")
