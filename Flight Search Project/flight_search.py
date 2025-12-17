import datetime
from API import creds
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = creds.FLIGHT_API_KEY
        self._api_secret = creds.FLIGHT_API_SECRET
        self._token = None

    def get_flight_data(self,origin_city_code,destination_city_code,from_date):
        headers = {
            "Authorization": "Bearer " + self._token,
        }
        endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = {
            "originLocationCode" : origin_city_code,
            "destinationLocationCode" : destination_city_code,
            "departureDate" : from_date.strftime("%Y-%m-%d"),
            "nonStop" : "true",
            "adults" : 1,
            "currencyCode" : "GBP",
            "max" : "10"
        }
        response = requests.get(url=endpoint, headers=headers, params=params)
        if response.status_code != 200:
            print(response.text)
        return response.json()

    def get_iata_code(self,city_name):
        params = {
            "keyword": city_name,
            "include": "AIRPORTS",
            "max" : 5
        }
        headers = {
            "Authorization": "Bearer " + self._token,
        }
        endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        response = requests.get(endpoint, params=params,headers=headers)
        city_data = response.json()["data"]
        try:
            iata_code = city_data[0]["iataCode"]
        except IndexError:
            print("No such city found!")
        else:
            return iata_code
        return None

    def get_new_token(self) -> str:
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
        token_data = response.json()
        self._token = token_data['access_token']
        return self._token