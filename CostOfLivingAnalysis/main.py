from src.real_estate import Real_Estate
from src.wages import Wages
from src.expenses import Expenses

# Constants
REAL_ESTATE_CSV = "./data/home_prices.csv"
WAGE_CSV = "./data/wages.csv"
EXPENSES_CSV = "./data/expenses.csv"

real_estate = Real_Estate()
wages = Wages()
expenses = Expenses()

# Update Data Sets
# real_estate.update_real_estate_data(file=REAL_ESTATE_CSV)
# wages.update_wage_data(file=WAGE_CSV)
# expenses.update_expense_data(file=EXPENSES_CSV)

# Fetch Data Sets
# real_estate_data = real_estate.obtain_real_estate_data(file=REAL_ESTATE_CSV)
wage_data = wages.obtain_wage_data(file=WAGE_CSV)
expenses_data = expenses.obtain_expense_data(file=EXPENSES_CSV)

# print(f"Current price of a 1-2 bedroom house: ${real_estate_data:,}")
print(f"Current average wage in Victoria: ${wage_data}/hour")
print(f"Current cost of living in Victoria: ${expenses_data:,}")
