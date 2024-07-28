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
        """Converts search result JSON data into declared variables.

        Args:
            airline (str): Airline matching ticket is with.
            bag_price (str): Cost of a checked bag.
            departure_airport (str): Departure airport code.
            departure_city (str): Departure city.
            arrival_airport (str): Arrival airport code.
            arrival_city (str): Arrival city.
            nights_in_destination (str): Number of nights in destination before return flight.
            flight_price (str): Cost for airfare (without baggage).
            departure_date (str): Date of departing flight.
            return_date (str): Date of returning flight.
            booking_link (str): Link to book flight.
        """
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
