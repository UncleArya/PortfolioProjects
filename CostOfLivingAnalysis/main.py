from src.real_estate import Real_Estate
from src.wages import Wages
from src.expenses import Expenses
from src.calculations import Calculations
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# Constants
REAL_ESTATE_CSV = "./data/home_prices.csv"
AVERAGE_WAGE_CSV = "./data/average_wages.csv"
EXPENSES_CSV = "./data/expenses.csv"

real_estate = Real_Estate()
wages = Wages()
expenses = Expenses()

app = Flask(__name__)
bootstrap = Bootstrap5(app)


# Fetch an update to all data sets
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
years_needed_to_pay_off_mortgage = calculations.years_to_pay_off_mortgage()
months_for_two_adults_down_payment = calculations.two_adults_down_payment()


# Flask App
@app.route("/")
def home():
    return render_template(
        "home.html",
        real_estate_data=real_estate_data,
        wage_data=wage_data,
        expenses_data=expenses_data,
        months_to_save_for_down_payment=months_to_save_for_down_payment,
        years_needed_to_pay_off_mortgage=years_needed_to_pay_off_mortgage,
        months_for_two_adults_down_payment=months_for_two_adults_down_payment,
    )


update_data_sets()

if __name__ == "__main__":
    app.run(debug=True)
