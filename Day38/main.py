import requests
import datetime
import json

WEIGHT = 100
HEIGHT = 200
AGE = 50
GENDER = "female"

sensitive_data = {}
with open('sensitive_data.json', 'r') as f:
    sensitive_data = json.load(f)

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {    
    "x-app-id": sensitive_data["100daysPython"]["x-app-id"],
    "x-app-key": sensitive_data["100daysPython"]["x-app-key"],
}

query = input("What did you workout today? ")

exercise_data = {
    "query": query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER,
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
workout_data = response.json()
# print(workout_data)



sheety_endpoint = sensitive_data["sheety_data"]["sheety_endpoint"]

sheety_data = {
    "workout": {
        "date": datetime.datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "exercise": workout_data["exercises"][0]["name"],
        "duration": workout_data["exercises"][0]["duration_min"],
        "calories": workout_data["exercises"][0]["nf_calories"],
    }
}

sheety_headers = {
    "Authorization": sensitive_data["sheety_data"]["Authorization"]
}

response = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_headers)
# print(response.text)
