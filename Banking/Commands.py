from abc import ABC, abstractmethod
from Banking.BankSystem import BankSystem


# Command Interface

class Command(ABC):
    """ Abstract command class serving as interface for all commands. """
    @abstractmethod
    def execute(self):
        """ Abstract method in order to execute specific command"""
        pass


# Concrete Commands


class AdvanceMonthCommand(Command):
    """ Command to advance bank system to next month """
    def execute(self):
        BankSystem.advance_month()


class DepositToSavingsCommand(Command):
    """ Command to deposit a specific amount into the savings account"""
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        BankSystem.deposit_to_savings(self.amount)


class WithdrawFromSavingsCommand(Command):
    """ Command to withdraw a specified amount from savings account"""
    def __init__(self, amount):
        self.amount = amount

    def execute(self):
        BankSystem.withdraw_from_savings(self.amount)


class CreateNewLoanCommand(Command):
    """ Command to create a new loan with a specific amount and interest rate"""
    def __init__(self, amount, interest_rate):
        self.amount = amount
        self.interest_rate = interest_rate

    def execute(self):
        BankSystem.create_new_loan(self.amount, self.interest_rate)


class PayLoanCommand(Command):
    """ Command to make payment towards a specified loan"""
    def __init__(self, loan_id, amount):
        self.loan_id = loan_id
        self.amount = amount

    def execute(self):
        BankSystem.pay_loan(self.loan_id, self.amount)


class ShowSavingsBalanceCommand(Command):
    """ Command to display the current savings account balance"""
    def execute(self):
        BankSystem.show_savings_balance()


class ShowLoanCommand(Command):
    """ Command to display the details of a specific loan"""
    def __init__(self, loan_id):
        self.loan_id = loan_id

    def execute(self):
        BankSystem.show_loan(self.loan_id)


class ShowAllLoansCommand(Command):
    """ Command to display details of all the loans"""
    def execute(self):
        BankSystem.show_all_loans()


class HelpCommand(Command):
    """ Command to display the help menu"""
    def execute(self):
        BankSystem.show_help()


class GenerateReportCommand(Command):
    """ Command to generate and display the bank report"""
    def execute(self):
        BankSystem.generate_report()
