from bs4 import BeautifulSoup
import requests
import csv

# URL & Headers
REAL_ESTATE_URL = "https://www.vreb.org/current-statistics#gsc.tab=0"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
ACCEPT_LANGAUGE = "en-CA,en-US;q=0.7,en;q=0.3"


class Real_Estate:
    def __init__(self):
        """Contains functions to update and recall real estate data."""
        self.real_estate_prices = []

    def update_real_estate_data(self, file):
        """Updates real estate data by scraping a real estate website and writing the listed prices to a CSV file.

        Args:
            file (str): path to csv file to write data to
        """
        self.csv_file = file
        webpage = requests.get(
            url=REAL_ESTATE_URL,
            headers={"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGAUGE},
        )
        soup = BeautifulSoup(webpage.text, "html.parser")
        prices = soup.select(".mls-stats-summary > div:nth-child(2) > div:nth-child(2) > div:nth-child(8)")
        # Remove unwanted formatting
        price_clean = int(prices[0].text.split("$")[-2].split(" ")[0].replace(",", ""))
        # Write to CSV file
        with open(self.csv_file, mode="w") as csv_file:
            real_estate_csv = csv.writer(csv_file)
            real_estate_csv.writerow([price_clean])

    def obtain_real_estate_data(self, file):
        """Returns the current average listed price for a condo saved to a csv file.

        Args:
            file (str): path to the csv file to read data from

        Returns:
            int: real estate price
        """
        self.csv_file = file
        with open(self.csv_file, mode="r") as csv_file:
            real_estate_total = sum(int(row[0]) for row in csv.reader(csv_file))
        return real_estate_total
