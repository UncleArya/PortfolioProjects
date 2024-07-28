# Files
from src.flight_data import FlightData

# Modules
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Constants
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_URL = "https://api.tequila.kiwi.com/v2/search"
HEADERS = {
    "apikey": KIWI_API_KEY,
}


# Flight Search
class FlightSearch:
    def __init__(self):
        """Contains the functions to interact with the Kiwi API."""
        pass

    def get_flight_price(
        self,
        departure_airport,
        arrival_airport,
        date_from,
        date_to,
        min_night_stay,
        max_night_stay,
        adults,
        ret_from_diff_city,
        ret_to_diff_city,
        currency,
        stopover_length,
        max_stopovers,
        max_sector_stopovers,
        enable_vi,
        limit,
        excluded_airlines
    ):
        """Uses the Kiwi Tequila API to obtain flight search information.

        Args:
            departure_airport (str): 3 character airport IATA code
            arrival_airport (str): 3 character airport IATA code or 2 digit country code
            date_from (str): dd/mm/yyyy
            date_to (str): dd/mm/yyyy
            min_night_stay (int): minimum length of stay in the destination
            max_night_stay (int): maximum length of stay in the destination
            adults (int): number of adult plane tickets
            ret_from_diff_city (bool): fly out of a different city than was flown into
            ret_to_diff_city (bool): fly into a different city than was flown out of
            currency (str): currency for pricing info
            stopover_length (str): maximum total layover time
            max_stopovers (int): maximum number of layovers for the whole journey
            max_sector_stopovers (int): maximum number of layovers for each leg of the journey
            enable_vi (bool): allows for combining airlines to get to the destination
            limit (int): number of search results to find
            excluded_airlines (list): list of airlines to exclude from search results

        Returns:
            json: API search results
        """
        flight_params = {
            "fly_from": departure_airport,
            "fly_to": arrival_airport,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": min_night_stay,
            "nights_in_dst_to": max_night_stay,
            "adults": adults,
            "ret_from_diff_city": ret_from_diff_city,
            "ret_to_diff_city": ret_to_diff_city,
            "curr": currency,
            "stopover_to": stopover_length,
            "max_stopovers": max_stopovers,
            "max_sector_stopovers": max_sector_stopovers,
            "enable_vi": enable_vi,
            "limit": limit,
            "select_airlines_exclude": True,
            "select_airlines": excluded_airlines,
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
