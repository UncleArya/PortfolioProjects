# Files
from src.flight_search import FlightSearch
from src.data_manager import DataManager
from src.notification_manager import NotificationManager

# Modules
import time

# Assign Class variables
data = DataManager()
flight_search = FlightSearch()

# Constants
DEPARTURES_LIST = []
EXCLUDED_AIRLINES_LIST = []
NOTIFICATION_LIST = []

# Variables
search_number = 1
are_errors = False
error_lines = []

# Get current destination list
destination_list = data.get_destination_data()

# Get current departures list
departures_data = data.get_departures_data()
for location in departures_data:
    DEPARTURES_LIST.append(location["code"])

# Get current list of excluded airlines
excluded_airlines = data.get_excluded_airlines()
for airline in excluded_airlines:
    EXCLUDED_AIRLINES_LIST.append(airline["code"])

# Get current search parameters
search_parameters = data.get_search_parameters()[0]
number_of_tickets = search_parameters["adults"]
return_from_different_city = search_parameters["returnFromDifferentCity"]
return_to_different_city = search_parameters["returnToDifferentCity"]
currency = search_parameters["currency"]
stopover_length = search_parameters["stopoverLength"]
max_stopovers = search_parameters["maxStopovers"]
max_sector_stopovers = search_parameters["maxSectorStopovers"]
virtually_interlined = search_parameters["virtuallyInterlined"]
number_of_results = search_parameters["limit"]

# Search for flight data from each departure airport in the list
for airport in DEPARTURES_LIST:
    # Search for flight data for each destination in the list
    for destination in destination_list:
        arrival_airport = destination["code"]
        date_from = destination["dateFrom"]
        date_to = destination["dateTo"]
        minimum_night_stay = destination["minimumNightStay"]
        maximum_night_stay = destination["maximumNightStay"]
        price_trigger = int(destination["priceTrigger"])

        print(
            f"{search_number}/{len(destination_list) * len(DEPARTURES_LIST)}: Searching for flights from {airport} to {destination['city']}..."
        )
        search_number += 1

        try:
            search_results = flight_search.get_flight_price(
                departure_airport=airport,
                arrival_airport=arrival_airport,
                date_from=date_from,
                date_to=date_to,
                min_night_stay=minimum_night_stay,
                max_night_stay=maximum_night_stay,
                adults=number_of_tickets,
                ret_from_diff_city=return_from_different_city,
                ret_to_diff_city=return_to_different_city,
                currency=currency,
                stopover_length=stopover_length,
                max_stopovers=max_stopovers,
                max_sector_stopovers=max_sector_stopovers,
                enable_vi=virtually_interlined,
                limit=number_of_results,
                excluded_airlines=EXCLUDED_AIRLINES_LIST,
            )

            flight_result = {
                "Airline": search_results.airline,
                "Baggage Cost": search_results.bag_price,
                "Departure Airport": search_results.departure_airport,
                "Departure City": search_results.departure_city,
                "Arrival Airport": search_results.arrival_airport,
                "Arrival City": search_results.arrival_city,
                "Nights in Destination": search_results.nights_in_destination,
                "Ticket Price": search_results.flight_price,
                "Departure Date": search_results.departure_date,
                "Return Date": search_results.return_date,
                "Booking Link": search_results.booking_link,
            }

            # Only add to notification list if found price is lower than price trigger in Google sheet
            if search_results.flight_price < price_trigger:
                print(f"Flight found from {airport} to {search_results.arrival_city}")
                NOTIFICATION_LIST.append(flight_result)

        # Find errors and add to notification list
        except AttributeError:
            # Skip instances where no flight between the 2 airports exists
            if flight_search.no_flight_found:
                pass

            else:
                print(f"Skipping {destination['city']}...")
                are_errors = True
                error_lines.append(destination["city"])

    # Pause for 2 minutes to stay within API limit rules
    time.sleep(120)

# Add a run date to the search history tab
data.update_search_history()

# Send email if error
if are_errors:
    NotificationManager("").error_email(error_content=f"Error in Flight Deals sheet for {error_lines}")

# If it finds at least one flight matching the criteria, email the flight details
if NOTIFICATION_LIST:
    print(f"A total of {len(NOTIFICATION_LIST)} flights have been found! Forwarding results now...")
    NotificationManager(NOTIFICATION_LIST).send_email()
