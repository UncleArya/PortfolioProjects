from bs4 import BeautifulSoup
import requests
import time
import csv

# URL & Headers
REAL_ESTATE_URL_START = "https://www.remax.ca/bc/victoria-real-estate?lang=en&pageNumber="
REAL_ESTATE_URL_END = "&priceMin=&priceMax=&pricePerSqftMin=&pricePerSqftMax=&priceType=0&sqftMin=&sqftMax=&lotSizeMin=&lotSizeMax=&bedsMin=1&bedsMax=2&bathsMin=&bathsMax=&featuredListings=&isRemaxListing=false&comingSoon=false&updatedInLastNumDays=&featuredLuxury=false&minImages=&house=false&townhouse=false&condo=false&rental=false&land=false&farm=false&duplex=false&cottage=false&other=false&commercial=false&commercialLease=false&vacantLand=false&hotelResort=false&businessOpportunity=false&rentalsOnly=false&commercialOnly=false&luxuryOnly=false&hasOpenHouse=false&hasVirtualOpenHouse=false&parkingSpacesMin=&parkingSpacesMax=&commercialSqftMin=&commercialSqftMax=&unitsMin=&unitsMax=&storiesMin=&storiesMax=&totalAcresMin=&totalAcresMax=&Agriculture=false&Automotive=false&Construction=false&Grocery=false&Hospitality=false&Hotel=false&Industrial=false&Manufacturing=false&Multi-Family=false&Office=false&Professional=false&Restaurant=false&Retail=false&Service=false&Transportation=false&Warehouse=false"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
ACCEPT_LANGAUGE = "en-CA,en-US;q=0.7,en;q=0.3"


class Real_Estate:
    def __init__(self):
        self.real_estate_prices = []

    def update_real_estate_data(self, file):
        self.csv_file = file

        for page in range(1, 3):
            webpage = requests.get(
                url=f"{REAL_ESTATE_URL_START}{page}{REAL_ESTATE_URL_END}",
                headers={"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGAUGE},
            )
            soup = BeautifulSoup(webpage.text, "html.parser")
            prices = soup.select(".listing-card_price__lEBmo > span")

            for price in prices:
                raw_price = price.text.replace("$", "").replace(",", "")
                if raw_price:
                    self.real_estate_prices.append(raw_price)

            print(f"Page {page} scraped...")

            time.sleep(10)

        with open(self.csv_file, mode="w") as csv_file:
            real_estate_csv = csv.writer(csv_file)
            for listing in self.real_estate_prices:
                real_estate_csv.writerow([listing])
