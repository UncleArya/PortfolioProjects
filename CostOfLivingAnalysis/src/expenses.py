from bs4 import BeautifulSoup
import requests
import csv

EXPENSES_URL = "https://www.movingwaldo.com/where-to-live/cost-of-living-victoria/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
ACCEPT_LANGAUGE = "en-CA,en-US;q=0.7,en;q=0.3"


class Expenses:
    def __init__(self):
        self.total_expenses = 0

    def update_expense_data(self, file):
        self.csv_file = file
        webpage = requests.get(url=EXPENSES_URL, headers={"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGAUGE})
        soup = BeautifulSoup(webpage.text, "html.parser")
        expenses = soup.select(".elementor-element-8961ada > div > p")
        expenses_raw = expenses[0].text
        expenses_clean = expenses_raw.split("$")[1].split(".")[0].replace(",", "")
        self.total_expenses = int(expenses_clean)
        with open(self.csv_file, mode="w") as csv_file:
            wages_csv = csv.writer(csv_file)
            wages_csv.writerow([self.total_expenses])

    def obtain_expense_data(self, file):
        self.csv_file = file
        with open(self.csv_file, mode="r") as csv_file:
            expenses_total = sum(int(row[0]) for row in csv.reader(csv_file))
            return expenses_total
