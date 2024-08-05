# Constants
INTEREST_RATE = 0.05
MINIMUM_WAGE = 17.40


class Calculations:
    def __init__(self, real_estate_data, wage_data, expenses_data):
        """Contains functions to execute various calculations.

        Args:
            real_estate_data (int): current cost for a condo
            wage_data (float): current average hourly wage for posted jobs
            expenses_data (int): current cost of living expense estimate
        """
        self.real_estate_data = real_estate_data
        self.down_payment_amount = real_estate_data * 0.1
        self.wage_data = wage_data
        self.expenses_data = expenses_data

    def average_wage_down_payment(self):
        """Time needed to save for a 10% down payment on a condo at average wage.

        Returns:
            float: months to save for down payment
        """
        savings_per_month = (self.wage_data * 173.33) - self.expenses_data
        months_to_save = round(self.down_payment_amount / savings_per_month, 1)
        return months_to_save

    def years_to_pay_off_mortgage(self):
        """Years needed to pay off a mortgage for a condo at average wage.

        Returns:
            float: years needed to pay off mortgage
        """
        months_to_pay_off_mortgage = 0
        # Remove 40% of expenses as rent no longer being paid
        savings_per_month = (self.wage_data * 173.33) - (self.expenses_data - (self.expenses_data * 0.4))
        principle_amount = self.real_estate_data - self.down_payment_amount
        # Calculate monthly payment and interest rate amounts
        while principle_amount > 0:
            principle_amount = principle_amount + (principle_amount * (INTEREST_RATE / 12)) - savings_per_month
            months_to_pay_off_mortgage += 1
        years = round((months_to_pay_off_mortgage / 12), 1)
        return years

    def two_adults_down_payment(self):
        """Months needed for two adults earning minimum wage to save for a 10% down payment on a condo.

        Returns:
            float: months to save for down payment
        """
        # Remove 40% of expenses for 1 person as rent is shared
        savings_per_month = ((MINIMUM_WAGE * 2) * 173.33) - (
            self.expenses_data + (self.expenses_data - (self.expenses_data * 0.4))
        )
        months_to_save = round(self.down_payment_amount / savings_per_month, 1)
        return months_to_save
