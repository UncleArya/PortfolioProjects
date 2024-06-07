# Files
from FlightPriceTracker.src.flight_data import FlightData

# Modules
import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Constants
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_URL = "https://api.tequila.kiwi.com/v2/search"
HEADERS = {
    "apikey": KIWI_API_KEY,
}
CURRENT_DATE = datetime.datetime.now()
ONE_YEAR_AHEAD = CURRENT_DATE + datetime.timedelta(days=365)


class FlightSearch:
    def get_flight_price(
        self,
        departure_airport,
        arrival_airport,
        date_from,
        date_to,
        min_night_stay,
        max_night_stay,
    ):
        flight_params = {
            "fly_from": departure_airport,
            "fly_to": arrival_airport,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": min_night_stay,
            "nights_in_dst_to": max_night_stay,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "select_airlines_exclude": True,
            "select_airlines": [],
            "adults": 1,
            "curr": "CAD",
            "stopover_to": "12:00",
            "max_stopovers": 2,
            "max_sector_stopovers": 1,
            "enable_vi": False,
            "limit": 1,
        }
        request_data = requests.get(url=KIWI_URL, headers=HEADERS, params=flight_params)
        try:
            data = request_data.json()["data"][0]
        except IndexError:
            print(f"No flights found for {departure_airport} to {arrival_airport}.")
            return None
        except KeyError:
            print(f"Error in spreadsheet for {departure_airport} to {arrival_airport}.")
            return None

        flight_data = FlightData(
            airline=data["airlines"],
            bag_price=data["bags_price"],
            departure_airport=data["flyFrom"],
            departure_city=data["cityFrom"],
            arrival_airport=data["flyTo"],
            arrival_city=data["cityTo"],
            nights_in_destination=data["nightsInDest"],
            flight_price=data["price"],
            departure_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][-1]["local_arrival"].split("T")[0],
            booking_link=data["deep_link"],
        )
        return flight_data
