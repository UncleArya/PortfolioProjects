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
SEARCH_PARAMETERS_SHEET_URL = "flightDeals/searchParameters"
EMAIL_SHEET_URL = "flightDeals/emails"
SEARCH_HISTORY_URL = "flightDeals/searchHistory"

# Authentication
HEADERS = {"Authorization": f"Bearer {BEARER_TOKEN}"}


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.search_param_data = {}
        self.email_data = {}

    def get_destination_data(self):
        raw_destination_data = requests.get(
            f"{SHEETY_URL}{DESTINATIONS_SHEET_URL}", headers=HEADERS
        ).json()
        self.destination_data = raw_destination_data["destinations"]
        return self.destination_data

    def get_search_parameters(self):
        raw_search_param_data = requests.get(
            f"{SHEETY_URL}{SEARCH_PARAMETERS_SHEET_URL}", headers=HEADERS
        ).json()
        self.search_param_data = raw_search_param_data["searchParameters"]
        return self.search_param_data

    def get_email_addresses(self):
        raw_email_data = requests.get(
            f"{SHEETY_URL}{EMAIL_SHEET_URL}", headers=HEADERS
        ).json()
        self.email_data = raw_email_data["emails"]
        return self.email_data

    def update_search_history(self):
        sheet_input = {
            "searchHistory": {"runDate": datetime.datetime.now().strftime("%x %X")}
        }
        requests.post(
            url=f"{SHEETY_URL}{SEARCH_HISTORY_URL}", json=sheet_input, headers=HEADERS
        )
