import datetime,time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import *
from notification_manager import NotificationManager

google_sheet_manager = DataManager()
flight_search_manager = FlightSearch()
token = flight_search_manager.get_new_token()
flight_search_manager._token = token
print(token)
sheet_data = google_sheet_manager.get_message()

customer_data = google_sheet_manager.get_customer_emails()
customer_emails = [data["emailAddress"] for data in customer_data["users"]]
print(customer_emails)

#----------------------------------------------PUT IATA CODE-----------------------------------------#
for flight in sheet_data["prices"]:
    if flight["iataCode"] == "":
        city_name = flight["city"]
        iata_code = flight_search_manager.get_iata_code(city_name)
        if iata_code is None:
            iata_code = "ERROR"
        json_payload = {"price": {
                "city": flight["city"],
                "iataCode": iata_code,
                "lowestPrice": flight["lowestPrice"]
            }}
        google_sheet_manager.put_data(json_payload,flight["id"])

#------------------------------------------------FLIGHT DATA------------------------------------------#
for flight in sheet_data["prices"]:
    origin_city_code = "LON"
    destination_city_code = flight["iataCode"]
    price = flight["lowestPrice"]
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    flight_data = flight_search_manager.get_flight_data(origin_city_code,destination_city_code,tomorrow)
    flight_data_manager = find_cheapest_flight(flight_data)

    print(f"{flight['city']}: £{flight_data_manager.price}")
    if flight_data_manager.price == "N/A":
        flight_data = flight_search_manager.get_flight_data(origin_city_code,destination_city_code,tomorrow,is_direct="false")
        flight_data_manager = find_cheapest_flight(flight_data)
        print(f"{flight['city']}: £{flight_data_manager.price}")
    if flight_data_manager.price == "N/A":
        continue
    if flight_data_manager.price <= price:
        notification_manager = NotificationManager(flight_data_manager.price,
                                                   flight_data_manager.origin_airport,
                                                   flight_data_manager.destination_airport,
                                                   flight_data_manager.out_date,
                                                   flight_data_manager.stops)
        notification_manager.send_emails(customer_email=customer_emails)
    # Slowing down requests to avoid rate limit
    time.sleep(2)


