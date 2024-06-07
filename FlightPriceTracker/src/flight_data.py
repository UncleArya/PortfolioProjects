class FlightData:
    def __init__(
        self,
        airline,
        bag_price,
        departure_airport,
        departure_city,
        arrival_airport,
        arrival_city,
        nights_in_destination,
        flight_price,
        departure_date,
        return_date,
        booking_link,
    ):
        self.airline = airline
        self.bag_price = bag_price
        self.departure_airport = departure_airport
        self.departure_city = departure_city
        self.arrival_airport = arrival_airport
        self.arrival_city = arrival_city
        self.nights_in_destination = nights_in_destination
        self.flight_price = flight_price
        self.departure_date = departure_date
        self.return_date = return_date
        self.booking_link = booking_link
