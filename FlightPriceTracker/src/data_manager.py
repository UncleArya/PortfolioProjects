# Modules
import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

# Constants
SHEETY_URL = os.environ.get("SHEETY_URL")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

DESTINATIONS_SHEET_URL = "flightDeals/destinations"
DEPARTURE_LIST_URL = "flightDeals/departureAirports"
EXCLUDED_AIRLINES_LIST_URL = "flightDeals/excludedAirlines"
SEARCH_PARAMETERS_SHEET_URL = "flightDeals/searchParameters"
EMAIL_SHEET_URL = "flightDeals/emails"
SEARCH_HISTORY_URL = "flightDeals/searchHistory"

# Authentication
HEADERS = {"Authorization": f"Bearer {BEARER_TOKEN}"}


class DataManager:
    def __init__(self):
        """Contains functions that interact with the Sheety API to GET and POST data."""
        self.destination_data = {}
        self.departures_data = {}
        self.excluded_airline_data = {}
        self.search_param_data = {}
        self.email_data = {}

    def get_destination_data(self):
        """Obtains the data from the destinations tab in the linked Google Sheet."""
        raw_destination_data = requests.get(f"{SHEETY_URL}{DESTINATIONS_SHEET_URL}", headers=HEADERS).json()
        self.destination_data = raw_destination_data["destinations"]
        return self.destination_data

    def get_departures_data(self):
        """Obtains the data from the departure_airports tab in the linked Google Sheet"""
        raw_departure_data = requests.get(f"{SHEETY_URL}{DEPARTURE_LIST_URL}", headers=HEADERS).json()
        self.departures_data = raw_departure_data["departureAirports"]
        return self.departures_data

    def get_excluded_airlines(self):
        """Obtains the data from the excluded_airlines tab in the linked Google Sheet"""
        raw_excluded_airlines_data = requests.get(f"{SHEETY_URL}{EXCLUDED_AIRLINES_LIST_URL}", headers=HEADERS).json()
        self.excluded_airline_data = raw_excluded_airlines_data["excludedAirlines"]
        return self.excluded_airline_data

    def get_search_parameters(self):
        """Obtains the data from the search_parameters tab in the linked Google Sheet."""
        raw_search_param_data = requests.get(f"{SHEETY_URL}{SEARCH_PARAMETERS_SHEET_URL}", headers=HEADERS).json()
        self.search_param_data = raw_search_param_data["searchParameters"]
        return self.search_param_data

    def get_email_addresses(self):
        """Obtains the data from the emails tab in the linked Google Sheet."""
        raw_email_data = requests.get(f"{SHEETY_URL}{EMAIL_SHEET_URL}", headers=HEADERS).json()
        self.email_data = raw_email_data["emails"]
        return self.email_data

    def update_search_history(self):
        """Writes data to the search_history tab in the linked Google Sheet."""
        sheet_input = {"searchHistory": {"runDate": datetime.datetime.now().strftime("%x %X")}}
        requests.post(url=f"{SHEETY_URL}{SEARCH_HISTORY_URL}", json=sheet_input, headers=HEADERS)
