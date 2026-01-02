import requests

OWM_endpoint = "http://api.openweathermap.org/data/2.5/forecast"

with open(file="api_key.txt.", mode="r") as f:
    api_key = f.read()

parameters = {
    "lat": -23.550520,
    "lon": -46.63330,
    "appid": api_key,
    "cnt": 40,
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

for three_hours_interval in weather_data["list"]:
    for three_hours_interval_weather in three_hours_interval["weather"]:
        condition_code = int(three_hours_interval_weather["id"])
        if condition_code < 700:
            will_rain = True

if will_rain:
    print("Bring an umbrella!")