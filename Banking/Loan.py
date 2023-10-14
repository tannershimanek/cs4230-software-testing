import config
from decimal import Decimal
from decimal import Decimal, ROUND_UP, ROUND_DOWN


class Loan:
    late_fee = Decimal(config.BANK_CONFIG.get('late_fee')).quantize(Decimal('0.01'), rounding=ROUND_DOWN)

    '''Loan object'''
    def __init__(self, amount, interest_rate) -> None:
        amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_UP)
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
        self.amount = amount 
        self.interest_rate = interest_rate
        self.payment_this_month = Decimal("0")

    def apply_interest(self) -> Decimal:
        monthly_interest = (self.amount * (self.interest_rate / Decimal("12"))) / Decimal("100")
        monthly_interest = monthly_interest.quantize(Decimal('0.01'), rounding=ROUND_UP)
        self.amount += monthly_interest
        return monthly_interest

    def apply_late_fee(self) -> None:
        rounded_late_fee = self.late_fee.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        self.amount += rounded_late_fee


    def pay(self, amount) -> None:
        amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        self.amount -= amount
        self.payment_this_month += amount

    def calculate_minimum_payment(self) -> Decimal:
        interest_due = (self.amount * (self.interest_rate/Decimal("100"))) / Decimal("12")
        one_percent_of_loan = Decimal("0.01") * self.amount
        #late_fee = 50 if self.payment_this_month < one_percent_of_loan else 0
        #min_payment = interest_due + one_percent_of_loan + late_fee
        min_payment = interest_due + one_percent_of_loan
        return max(min_payment, Decimal("10"))

    def reset_monthly_payment(self) -> None:
        self.payment_this_month = Decimal("0")
