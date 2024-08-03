from src.real_estate import Real_Estate

# Constants
REAL_ESTATE_CSV = "./data/home_prices.csv"

real_estate = Real_Estate()
real_estate.update_real_estate_data(file=REAL_ESTATE_CSV)
