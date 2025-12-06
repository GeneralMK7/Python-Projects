MY_LAT = 17.385044
MY_LONG = 78.486671

import datetime as dt
import requests

parameters ={
    'lat':MY_LAT,
    'lng':MY_LONG,
    'formatted': 0
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise,sunset)

print(dt.datetime.now().hour)