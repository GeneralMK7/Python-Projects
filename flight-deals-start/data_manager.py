import requests
from API import creds

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_data = {}
        self.sheety_endpoint = f"https://api.sheety.co/{creds.SHETTY_APP_USERNAME}/flightDeal/prices"
        self.headers = {
            "Authorization": "Bearer " + creds.SHETTY_APP_TOKEN1
        }


    def get_message(self):
        response = requests.get(url=self.sheety_endpoint,headers=self.headers)
        response.raise_for_status()
        self.get_data = response.json()
        return self.get_data

    def put_data(self,json_payload,obj_id):
        put_endpoint = f"{self.sheety_endpoint}/{obj_id}"
        response = requests.put(url=put_endpoint,json=json_payload,headers=self.headers)

