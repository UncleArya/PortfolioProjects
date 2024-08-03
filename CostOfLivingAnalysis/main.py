from src.real_estate import Real_Estate
from src.wages import Wages

# Constants
REAL_ESTATE_CSV = "./data/home_prices.csv"

real_estate = Real_Estate()
wages = Wages()

real_estate.update_real_estate_data(file=REAL_ESTATE_CSV)

print(wages.obtain_wage_data())
