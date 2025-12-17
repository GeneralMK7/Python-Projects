from API import creds
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self,price,origin,destination,from_date):
        self.price = price
        self.origin = origin
        self.destination = destination
        self.from_date = from_date

    def send_notification(self):
        message = (f"Low Price Alert! Only {self.price} to fly from "
                   f"{self.origin} to {self.destination},on {self.from_date}")
        client = Client(creds.account_sid, creds.auth_token)

        message = client.messages.create(
            body=message,
            from_="+18125613420",
            to="+919666225131",
        )