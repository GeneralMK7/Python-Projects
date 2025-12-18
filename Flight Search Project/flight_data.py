def find_cheapest_flight(data):
    if data is None or data["meta"]["count"] == 0:
        print("No flight data")
        return FlightData("N/A","N/A","N/A","N/A","N/A")

    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    from_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    stops = len(first_flight["itineraries"][0]["segments"])
    cheapest_flight = FlightData(lowest_price, origin, destination,from_date,stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            stops = len(flight["itineraries"][0]["segments"])
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date,stops)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,origin_airport,destination_airport,out_date,stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.stops = stops
