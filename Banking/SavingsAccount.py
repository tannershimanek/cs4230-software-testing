from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP # Importing decimal for rounding/precision 

class SavingsAccount:
    def __init__(self, interest_rate):
        self.balance = Decimal('0')
        self.interest_rate = Decimal(str(interest_rate))

    def deposit(self, amount):
        amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        if amount <= 0:
            return "Deposit amount must be a positive value."
        if amount > 1_000_000:
            return "Deposit cannot exceed $1,000,000."
        self.balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        if amount <= 0:
            return "Withdrawal amount must be a positive value."
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}" 
        else:
            return "Insufficient funds!"

    def apply_interest(self):
        monthly_interest_rate = self.interest_rate / Decimal("12")
        interest = self.balance * monthly_interest_rate
        interest = interest.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        self.balance += interest
        return f"Applied ${interest:.2f} interest. New savings balance: ${self.balance:.2f}"