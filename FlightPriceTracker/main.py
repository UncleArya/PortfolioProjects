# Modules & Files
from FlightPriceTracker.src.flight_search import FlightSearch
from FlightPriceTracker.src.data_manager import DataManager
from FlightPriceTracker.src.notification_manager import NotificationManager


# Assign Class variables
data = DataManager()
flight_search = FlightSearch()

# Constants
DEPARTURE_AIRPORT = "YVR"
NOTIFICATION_LIST = []

# Variables
search_number = 1
are_errors = False
error_lines = []

# Get current destination list and search parameters (saved in Google sheet)
destination_list = data.get_destination_data()

# Search for flight data for each destination in the list
for destination in destination_list:
    arrival_airport = destination["code"]
    date_from = destination["dateFrom"]
    date_to = destination["dateTo"]
    minimum_night_stay = destination["minimumNightStay"]
    maximum_night_stay = destination["maximumNightStay"]
    price_trigger = int(destination["priceTrigger"])

    print(
        f"{search_number}/{len(destination_list)}: Searching for flights to {destination['city']}..."
    )
    search_number += 1

    try:
        search_results = flight_search.get_flight_price(
            departure_airport=DEPARTURE_AIRPORT,
            arrival_airport=arrival_airport,
            date_from=date_from,
            date_to=date_to,
            min_night_stay=minimum_night_stay,
            max_night_stay=maximum_night_stay,
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
            NOTIFICATION_LIST.append(flight_result)

    # Find errors and add to notification list
    except AttributeError:
        print(f"Skipping {destination}...")
        are_errors = True
        error_lines.append(destination["city"])

# Add a run date to the search history tab
data.update_search_history()

# Send email if error
if are_errors:
    NotificationManager("").error_email(
        error_content=f"Error in Flight Deals sheet for {error_lines}"
    )

# If it finds at least one flight matching the criteria, email the flight details
if NOTIFICATION_LIST:
    NotificationManager(NOTIFICATION_LIST).send_email()
