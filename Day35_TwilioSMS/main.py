import os
from twilio.rest import Client
import requests

OWM_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
parameters = {
    "lat": -23.550520,
    "lon": -46.63330,
    "appid": api_key,
    "cnt": 4,
}
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for three_hours_interval in weather_data["list"]:
    for three_hours_interval_weather in three_hours_interval["weather"]:
        condition_code = int(three_hours_interval_weather["id"])
        if condition_code < 700:
            will_rain = True

if will_rain:
    print("Bring an umbrella!")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG016966014a8687880aea2dd8df0b2fb3',
        body='Vai chover nas próximas 12 horas em São Paulo. É bom levar guarda chuva.',
        to='+5511995958918'
    )
    print(message.status)
