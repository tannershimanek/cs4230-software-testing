class SavingsAccount:
    def __init__(self, interest_rate):
        self.balance = 0
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount == 0:
            return "Please make an actual deposit."
        if amount < 0:
            return "Deposit amount cannot be negative."
        if amount > 1000000:
            return "Deposit cannot exceed $1,000,000."
        self.balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount < 0:
            return "Withdrawal amount may not be negative."
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Insufficient funds!"

    def apply_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        return f"Applied ${interest:.2f} interest. New savings balance: ${self.balance:.2f}"
