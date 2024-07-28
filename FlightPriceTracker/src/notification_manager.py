# Modules
import smtplib
from email.message import EmailMessage
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Variables
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SENDING_EMAIL = os.environ.get("SENDING_EMAIL")
RECEIVING_EMAIL = os.environ.get("RECEIVING_EMAIL")
CURRENT_DATE = datetime.datetime.now()


class NotificationManager:
    def __init__(self, flight_results):
        """Contains the functions to manage sending emails.

        Args:
            flight_results (list): Contains a list of dictionaries that contain search results that have triggered an email.
        """
        self.flight_results = flight_results

    def compose_email(self):
        """Takes dictionary entries and turns them into readable HTML emails."""
        result_num = 1
        messages_as_list = [
            f"<h3>Deals for the week of: {CURRENT_DATE.strftime('%B %d, %Y')}</h3>"
            f"<p><strong>Total fights found: {len(self.flight_results)}</strong><br></p>"
        ]
        for result in self.flight_results:
            email_body = f"""
                <h3>Flight #{result_num}</h3>
                <p><strong>Ticket Price:</strong> ${result["Ticket Price"]}<br>
                <strong>Destination:</strong> {result["Arrival City"]} ({result["Arrival Airport"]})<br>
                <strong>Departing:</strong> {result["Departure City"]} ({result["Departure Airport"]})<br>
                <strong>Departure Date:</strong> {result["Departure Date"]}<br>
                <strong>Return Date:</strong> {result["Return Date"]}<br>
                <strong>Nights in Destination:</strong> {result["Nights in Destination"]}<br>
                <strong>Airline:</strong> {result["Airline"][0]}<br>
                <strong>Baggage Cost:</strong> ${round(result["Baggage Cost"]["1"])}<br>
                <strong><a href={result["Booking Link"]}>Booking Link</a></strong></p>
                <p></p>
                """
            messages_as_list.append(email_body)
            result_num += 1
        full_message = "".join(messages_as_list)
        return full_message

    def send_email(self):
        """Sends the created email."""
        message = EmailMessage()
        message["From"] = SENDING_EMAIL
        message["To"] = RECEIVING_EMAIL
        message["Subject"] = f"Flight Deals for {CURRENT_DATE.strftime('%B %d')}"
        message.set_content(self.compose_email(), subtype="html")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDING_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=SENDING_EMAIL,
                to_addrs=RECEIVING_EMAIL,
                msg=message.as_string(),
            )

    def error_email(self, error_content):
        """Sends an email when an error has occurred in the process of obtaining search results."""
        error_message = EmailMessage()
        error_message["From"] = SENDING_EMAIL
        error_message["To"] = RECEIVING_EMAIL
        error_message["Subject"] = "Error in Flight Deals Sheet"
        error_message.set_content(error_content, subtype="html")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDING_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=SENDING_EMAIL,
                to_addrs=RECEIVING_EMAIL,
                msg=error_message.as_string(),
            )
