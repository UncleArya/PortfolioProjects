from bs4 import BeautifulSoup
import requests
import csv
import unicodedata
import statistics

# URL & Headers
JOB_LISTINGS_URL_START = "https://www.glassdoor.ca/Job/victoria-jobs-SRCH_IL.0,8_IC2279563.htm?sortBy=date_desc"
AVERAGE_SALARY_URL = "https://ca.talent.com/salary?job=victoria+bc"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
ACCEPT_LANGAUGE = "en-CA,en-US;q=0.7,en;q=0.3"


class Wages:
    def __init__(self):
        self.wages = []

    def get_first_wage_data_source(self):
        webpage = requests.get(
            url=f"{JOB_LISTINGS_URL_START}",
            headers={"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGAUGE},
        )
        soup = BeautifulSoup(webpage.text, "html.parser")
        salaries = soup.select(".jobCard > div > .JobCard_salaryEstimate__arV5J")

        for salary in salaries:
            salary_clean = unicodedata.normalize("NFKD", salary.text)
            salary_raw = salary_clean.split(" ")[0].replace("$", "")
            if len(salary_raw) < 5:
                annual_raw = salary_raw.replace("K", "")
                annual_conversion = int(annual_raw) * 1000
                hourly_rate = round(((annual_conversion / 52) / 40), 2)
                self.wages.append(hourly_rate)
            else:
                self.wages.append(float(salary_raw))
        print(self.wages)
        wage = statistics.mean(self.wages)
        return wage

    def get_second_wage_data_source(self):
        webpage = requests.get(
            url=f"{AVERAGE_SALARY_URL}",
            headers={"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGAUGE},
        )
        soup = BeautifulSoup(webpage.text, "html.parser")
        wage = float(soup.select(".c-card__stats-info > b")[3].text.replace("$", ""))
        return wage

    def update_wage_data(self, file):
        self.csv_file = file
        source_1 = self.get_first_wage_data_source()
        source_2 = self.get_second_wage_data_source()
        average_wage = round(((source_1 + source_2) / 2), 2)
        with open(self.csv_file, mode="w") as csv_file:
            wages_csv = csv.writer(csv_file)
            wages_csv.writerow([average_wage])

    def obtain_wage_data(self, file):
        self.csv_file = file
        with open(self.csv_file, mode="r") as csv_file:
            wages_total = sum(float(row[0]) for row in csv.reader(csv_file))
            return wages_total
