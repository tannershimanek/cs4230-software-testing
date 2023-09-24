from abc import ABC, abstractmethod
from BankSystem import BankSystem


# Command Interface

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete Commands


class AdvanceMonthCommand(Command):
    def execute(self):
        BankSystem.advance_month()


class CreateSavingsAccountCommand(Command):
    def execute(self):
        BankSystem.create_savings_account()


class DepositToSavingsCommand(Command):
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        BankSystem.deposit_to_savings(self.amount)


class WithdrawFromSavingsCommand(Command):
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        BankSystem.withdraw_from_savings(self.amount)


class CreateNewLoanCommand(Command):
    def __init__(self, amount, interest_rate):
        self.amount = amount
        self.interest_rate = interest_rate

    def execute(self):
        BankSystem.create_new_loan(self.amount, self.interest_rate)


class PayLoanCommand(Command):
    def __init__(self, loan_id, amount):
        self.loan_id = loan_id
        self.amount = amount

    def execute(self):
        BankSystem.pay_loan(self.loan_id, self.amount)


class ShowSavingsBalanceCommand(Command):
    def execute(self):
        BankSystem.show_savings_balance()


class ShowLoanCommand(Command):
    def __init__(self, loan_id):
        self.loan_id = loan_id

    def execute(self):
        BankSystem.show_loan(self.loan_id)


class ShowAllLoansCommand(Command):
    def execute(self):
        BankSystem.show_all_loans()


class HelpCommand(Command):
    def execute(self):
        BankSystem.show_help()


class GenerateReportCommand(Command):
    def execute(self):
        BankSystem.generate_report()
