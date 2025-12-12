import requests
from twilio.rest import Client
from WeatherAPI import creds

parameters = {
    "lat" : 4.284556,
    "lon" : 96.943119,
    "appid" : creds.API_KEY,
    "cnt" : 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
first_one = weather_data["list"][0]["weather"][0]["id"]
second_one = weather_data["list"][1]["weather"][0]["id"]
third_one = weather_data["list"][2]["weather"][0]["id"]
fourth_one = weather_data["list"][3]["weather"][0]["id"]

if any(x < 700 for x in [first_one, second_one, third_one, fourth_one]):
    client = Client(creds.account_sid, creds.auth_token)

    message = client.messages.create(
        body="Its going to rain today. So Don't forget to take an umbrella☔ with you",
        from_="+18125613420",
        to="+919666225131",
    )
