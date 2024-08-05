from src.real_estate import Real_Estate
from src.wages import Wages
from src.expenses import Expenses
from src.calculations import Calculations

# Constants
REAL_ESTATE_CSV = "./data/home_prices.csv"
AVERAGE_WAGE_CSV = "./data/average_wages.csv"
EXPENSES_CSV = "./data/expenses.csv"

real_estate = Real_Estate()
wages = Wages()
expenses = Expenses()


def update_data_sets():
    """Updates all 3 data sets and writes current data to respective CSV files."""
    real_estate.update_real_estate_data(file=REAL_ESTATE_CSV)
    wages.update_wage_data(file=AVERAGE_WAGE_CSV)
    expenses.update_expense_data(file=EXPENSES_CSV)


# Fetch Data Sets
real_estate_data = real_estate.obtain_real_estate_data(file=REAL_ESTATE_CSV)
wage_data = wages.obtain_wage_data(file=AVERAGE_WAGE_CSV)
expenses_data = expenses.obtain_expense_data(file=EXPENSES_CSV)

# Fetch Calculations
calculations = Calculations(real_estate_data=real_estate_data, wage_data=wage_data, expenses_data=expenses_data)
months_to_save_for_down_payment = calculations.average_wage_down_payment()
years_needed_to_pay_off_mortage = calculations.years_to_pay_off_mortgage()
months_for_two_adults_down_payment = calculations.two_adults_down_payment()

print(f"Current price of a condo: ${real_estate_data:,}")
print(f"Current average wage in Victoria: ${wage_data}/hour")
print(f"Current cost of living in Victoria: ${expenses_data:,}")
print(
    f"Time needed to save for a 10% down payment on a condo at average wage: {months_to_save_for_down_payment} months"
)
print(f"Years needed to pay off a mortgage for a condo at average wage: {years_needed_to_pay_off_mortage} years")
print(
    f"Months needed for two adults earning minimum wage to save for a 10% down payment on a condo: {months_for_two_adults_down_payment} months"
)
