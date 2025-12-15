from API import creds

APP_ID = creds.APP_BREWERY_ID
APP_KEY = creds.APP_BREWERY_KEY
APP_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

import requests,datetime
user_answer = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    'Authorization': 'Bearer ' + creds.SHETTY_APP_TOKEN,
}
parameters = {
    "query" : user_answer,
    "weight_kg": 70,
    "height_cm": 175,
    "age": 19,
    "gender": "male"
}

response = requests.post(url=APP_ENDPOINT, json=parameters,headers=headers)
workout_data = response.json()["exercises"][0]
today = datetime.date.today()
time = datetime.datetime.now()
json_payload = {
    "workout" : {
        "date" : today.strftime("%d/%m/%Y"),
        "time" : time.strftime("%H:%M:%S"),
        "exercise" : workout_data["name"].title(),
        "duration" : workout_data["duration_min"],
        "calories" : workout_data["nf_calories"]
    }
}
put_endpoint = f"https://api.sheety.co/{creds.SHETTY_APP_USERNAME}/workoutTracking/workouts"
put_response = requests.post(url=put_endpoint, json=json_payload,headers=headers)
print(put_response.text)