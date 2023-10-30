import config
from decimal import Decimal, ROUND_UP, ROUND_DOWN


class Loan:
    late_fee = Decimal(config.BANK_CONFIG.get('late_fee')).quantize(Decimal('0.01'), rounding=ROUND_DOWN)

    def __init__(self, amount, interest_rate) -> None:
        """ 
        Initializes a Loan object with given amount and interest rate. 

        """
        amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_UP)
        interest_rate = Decimal(interest_rate)

        if amount == Decimal("0"):
            raise ValueError("Loan amount cannot be zero")
        if amount < Decimal("0"):
            raise ValueError("Loan amount cannot be negative")
        if amount < Decimal("500"):
            raise ValueError("Loan amount cannot be less than 500")
        if amount > Decimal("50000"):
            raise ValueError("Loan amount cannot be greater than 50,000")
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
        """ Applies monthly interest to the loan and returns monthly interest amount. """
        monthly_interest = (self.amount * (self.interest_rate / Decimal("12"))) / Decimal("100")
        monthly_interest = monthly_interest.quantize(Decimal('0.01'), rounding=ROUND_UP)
        self.amount += monthly_interest
        return monthly_interest

    def apply_late_fee(self) -> None:
        """ Applies a late fee to the loan. """
        rounded_late_fee = self.late_fee.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        self.amount += rounded_late_fee 


    def pay(self, amount) -> None:
        """ Processes a payment towards the loan. """
        amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        if amount == Decimal("0"):
            raise ValueError("Payment amount cannot be zero")
        if amount < Decimal("0"):
            raise ValueError("Payment amount cannot be negative")
        if amount > self.amount:
            raise ValueError("Payment amount cannot be greater than loan amount")

        self.amount -= amount
        self.payment_this_month += amount

    def calculate_minimum_payment(self) -> Decimal:
        """ Calculates and returns the minimum payment due for the current month. """
        interest_due = (self.amount * (self.interest_rate/Decimal("100"))) / Decimal("12")
        one_percent_of_loan = Decimal("0.01") * self.amount
        min_payment = interest_due + one_percent_of_loan
        return max(min_payment, Decimal("10"))

    def reset_monthly_payment(self) -> None:
        """ Resets payment for current month to zero. """
        self.payment_this_month = Decimal("0")
