import config
from decimal import Decimal

class Loan:
    late_fee = Decimal(config.BANK_CONFIG.get('late_fee'))

    '''Loan object'''
    def __init__(self, amount, interest_rate) -> None:
        amount = Decimal(amount)
        interest_rate = Decimal(interest_rate)

        if amount == Decimal("0"):
            raise ValueError("Loan amount cannot be zero")
        if amount < Decimal("0"):
            raise ValueError("Loan amount cannot be negative")
        self.amount = amount
        if interest_rate == Decimal("0"):
            raise ValueError("Interest rate cannot be zero")
        if interest_rate < Decimal("0"):
            raise ValueError("Interest rate cannot be negative")
        if interest_rate > Decimal("18"):
            raise ValueError("Interest rate cannot be more than 18%")
        self.interest_rate = interest_rate
        self.payment_this_month = Decimal("0")

    def apply_interest(self) -> float:
        interest = (self.amount * (self.interest_rate / Decimal("12"))) / Decimal("100")
        self.amount += interest
        return interest

    def apply_late_fee(self) -> None:
        self.amount += self.late_fee

    def pay(self, amount) -> None:
        amount = Decimal(amount)
        self.amount -= amount
        self.payment_this_month += amount

    def calculate_minimum_payment(self) -> float:
        interest_due = (self.amount * (self.interest_rate/Decimal("100"))) / Decimal("12")
        one_percent_of_loan = Decimal("0.01") * self.amount
        #late_fee = 50 if self.payment_this_month < one_percent_of_loan else 0
        #min_payment = interest_due + one_percent_of_loan + late_fee
        min_payment = interest_due + one_percent_of_loan
        return max(min_payment, Decimal("10"))

    def reset_monthly_payment(self) -> None:
        self.payment_this_month = Decimal("0")
