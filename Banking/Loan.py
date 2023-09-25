class Loan:
    '''Loan object'''
    def __init__(self, amount, interest_rate):
        if amount == 0:
            raise ValueError("Loan amount cannot be zero")
        if amount < 0:
            raise ValueError("Loan amount cannot be negative")
        self.amount = amount
        self.interest_rate = interest_rate
        self.payment_this_month = 0

    def apply_interest(self):
        interest = (self.amount * (self.interest_rate / 12)) / 100
        self.amount += interest
        return interest

    def apply_late_fee(self):
        self.amount += 50

    def pay(self, amount):
        self.amount -= amount
        self.payment_this_month += amount

    def calculate_minimum_payment(self):
        interest_due = (self.amount * self.interest_rate) / 100
        one_percent_of_loan = 0.01 * self.amount
        late_fee = 50 if self.payment_this_month == 0 else 0
        min_payment = interest_due + one_percent_of_loan + late_fee
        return max(min_payment, 10)

    def reset_monthly_payment(self):
        self.payment_this_month = 0
