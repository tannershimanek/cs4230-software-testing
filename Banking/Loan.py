import config

class Loan:
    late_fee = config.BANK_CONFIG.get('late_fee')

    '''Loan object'''
    def __init__(self, amount, interest_rate) -> None:
        if amount == 0:
            raise ValueError("Loan amount cannot be zero")
        if amount < 0:
            raise ValueError("Loan amount cannot be negative")
        self.amount = amount
        if interest_rate == 0:
            raise ValueError("Interest rate cannot be zero")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative")
        if interest_rate > 18:
            raise ValueError("Interest rate cannot be more than 18%")
        self.interest_rate = interest_rate
        self.payment_this_month = 0

    def apply_interest(self) -> float:
        interest = (self.amount * (self.interest_rate / 12)) / 100
        self.amount += interest
        return interest

    def apply_late_fee(self) -> None:
        self.amount += self.late_fee

    def pay(self, amount) -> None:
        self.amount -= amount
        self.payment_this_month += amount

    def calculate_minimum_payment(self) -> float:
        interest_due = (self.amount * (self.interest_rate/100)) / 12
        one_percent_of_loan = 0.01 * self.amount
        #late_fee = 50 if self.payment_this_month < one_percent_of_loan else 0
        #min_payment = interest_due + one_percent_of_loan + late_fee
        min_payment = interest_due + one_percent_of_loan
        return max(min_payment, 10)

    def reset_monthly_payment(self) -> None:
        self.payment_this_month = 0
