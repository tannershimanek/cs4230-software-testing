import config
CONFIG = config.BANK_CONFIG

class Loan:
    def __init__(self, id, balance) -> None:
        self.id = id + CONFIG.get('loan_key')  # Will also need the current loan number
        self.interest_rate = CONFIG.get('interest_rate')
        self.balance = balance
        self.interest_added = 0
        self.late_fee = True

    def __str__(self):
        return f"Loan (ID = {self.id}, Balance = {self.balance}, IntRate = {self.interest_rate:.0%})"