import time
import requests
from datetime import datetime
import smtplib

MY_LAT = -22.380544
MY_LNG = -47.579136

def send_email():
    email = "mxm.0000001@gmail.com"
    with open(file="password.txt", mode='r') as f:
        password = f.read()

    connection = smtplib.SMTP("")
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
    )

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

iss_position = (iss_longitude, iss_latitude)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_time = sunrise.split("T")[1].split("+")[0].split(":")
sunset_time = sunset.split("T")[1].split("+")[0].split(":")

datetime_now_time = datetime.now().time()

while True:
    time.sleep(60)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        print("ISS is close. Checking if it is past sunrise/sunset,")

        if int(sunrise_time[0]) > datetime_now_time.hour and int(sunrise_time[1]) > datetime_now_time.minute and int(sunrise_time[2]) > datetime_now_time.second:
            print("It's before sunrise. Try looking up!")
            send_email()
        elif int(sunset_time[0]) < datetime_now_time.hour and int(sunset_time[1]) < datetime_now_time.minute and int(sunset_time[2]) < datetime_now_time.second:
            print("It's past sunset. See if you can find the ISS!")
            send_email()
        else:
            print("It's past sunrise but before sunset. You probably won't see the ISS :(")
    else:
        print("ISS is far.")

