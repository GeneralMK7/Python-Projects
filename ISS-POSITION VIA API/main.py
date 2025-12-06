import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 51.2420 # Your latitude
MY_LONG = 42.3419 # Your longitude

def is_near():
    position_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    position_response.raise_for_status()
    position_data = position_response.json()

    iss_latitude = float(position_data["iss_position"]["latitude"])
    iss_longitude = float(position_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset >= time_now <= sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if is_near() and is_night():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            email = "your-email"
            password = "your-password"
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(from_addr=email,
                                to_addrs="madhukiran.golla.personal@gmail.com",
                                msg="Subject: Information Reg. ISS Position\n\n"
                                    "Hey! Look Up!!")

