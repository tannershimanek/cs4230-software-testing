from Banking.Loan import Loan
from Banking.SavingsAccount import SavingsAccount
import config
from decimal import Decimal, InvalidOperation


class BankSystem:

    """
    Represents a bank system that manages savings accounts and loans.

    """
    savings = SavingsAccount(config.BANK_CONFIG.get('savings_rate'))
    late_fee = config.BANK_CONFIG.get('late_fee')
    loans = {}
    num_loans = 0
    current_loan_number = 0
    current_month = 1
    transactions = []

    @classmethod
    def advance_month(self):
        """
        Advances the bank system by one month, applies interest, fees,
        and generates monthly report.

        """
        self.current_month += 1
        print(f"Advanced to month {self.current_month}\n")

        for loan_id, loan in self.loans.items():
            print(f"Loan {loan_id} payment: ${loan.payment_this_month}")
            if loan.payment_this_month < loan.calculate_minimum_payment():
                loan.apply_late_fee()
                self.log_transaction(
                    f"Applied ${self.late_fee} late fee to Loan {loan_id}. New balance: ${loan.amount:.2f}")
                print(
                    f"Applied ${self.late_fee} late fee to Loan {loan_id}. New balance: ${loan.amount:.2f}")

        self.process_loan_interest()
        self.process_savings_interest()

        for loan in self.loans.values():
            loan.reset_monthly_payment()

        self.generate_report()

    @classmethod
    def log_transaction(self, description):
        """Logs a transaction to the transactions list for the bank report."""
        self.transactions.append(f"Month {self.current_month}: {description}")

    @classmethod
    def deposit_to_savings(self, amount):
        """ Deposits specified amount to the savings account.
            Args: amount (Decimal): Amount to be deposited.
        """
        message = self.savings.deposit(amount)
        self.log_transaction(message)
        print(message)

    @classmethod
    def withdraw_from_savings(self, amount):
        """ Withdraws specified amount to the savings account.
            Args: amount (Decimal): Amount to be withdrawn.
        """
        message = self.savings.withdraw(amount)
        self.log_transaction(message)
        print(message)

    @classmethod
    def process_savings_interest(self):
        """ Processes and applies interest to the savings account."""
        message = self.savings.apply_interest()
        self.log_transaction(message)
        print(message)

    @classmethod
    def show_savings_balance(self):
        """Displays the current savings account balance."""
        print(f"Savings balance: ${Decimal(str(self.savings.balance)):.2f}")

    @classmethod
    def create_new_loan(self, amount, interest_rate):
        """ Creates a new loan w/ specified amount and interest rate."""
        try:
            amount = Decimal(amount)
            interest_rate = Decimal(interest_rate)
        except ValueError:
            print("Invalid input types for loan amount or interest rate.")
            return

        if len(self.loans) >= 3:
            print("Maximum number of loans reached. Cannot create a new loan.")
            return

        if Decimal('500') <= amount <= Decimal('50000'):
            loan_id = self.current_loan_number + 1
            self.current_loan_number += 1
            self.loans[loan_id] = Loan(amount, interest_rate)
            print(
                f"Created new loan with ID {loan_id} for ${amount} at {interest_rate}% interest rate")
        else:
            print(
                "Loan amount is invalid. Please ensure amount is between $500 and $50,000.")

    @classmethod
    def pay_loan(self, loan_id, amount):
        """Pays the given amount to the given loan from the savings account."""
        try:
            loan_id = int(loan_id)
            amount = Decimal(amount)
        except ValueError:
            print("Invalid loan ID or amount. Please enter numerical values.")
            return
        if amount > Decimal(str(self.savings.balance)):
            print("Payment amount exceeds savings balance. Payment not processed.")
            return

        if loan_id in self.loans:
            loan = self.loans[loan_id]
            min_payment = loan.calculate_minimum_payment()

            if amount > loan.amount:
                print(
                    f"Payment is greater than the loan amount. Please pay an amount up to ${loan.amount:.2f}.")
                return

            if amount < (min_payment - loan.payment_this_month):
                print(f"Minimum payment still not met. You will be charged a ${self.late_fee:.2f} late fee if the minimum payment is not met.")
                print(f"Minimum required payment is ${min_payment:.2f}.")

            loan.pay(amount)

            # Subtract the payment amount from the savings balance
            self.savings.withdraw(amount)
            self.log_transaction(
                f"Paid ${amount:.2f} for loan {loan_id}. Remaining amount: ${loan.amount:.2f}")

            if loan.amount < Decimal('0.01'):
                self.loans.pop(loan_id)
                self.log_transaction(f"Loan {loan_id} paid off!")
                print(f"Loan {loan_id} paid off!")
            else:
                print(
                    f"Paid ${amount:.2f} for loan {loan_id}. Remaining amount: ${loan.amount:.2f}")
        else:
            print("Invalid loan ID!")

    @classmethod
    def process_loan_interest(self):
        """ Processes and applies interest to all loans"""
        for loan_id, loan in self.loans.items():
            try:
                interest = Decimal(loan.apply_interest())
            except InvalidOperation:
                print(f"Invalid interest value for loan {loan_id}. Skipping.")
                continue

            self.log_transaction(
                f"Applied ${interest:.2f} interest to loan {loan_id}. New balance: ${loan.amount:.2f}")
            print(
                f"Applied ${interest:.2f} interest to loan {loan_id}. New balance: ${loan.amount:.2f}")

    @classmethod
    def show_loan(self, loan_id):
        """Shows the given loan."""
        if loan_id in self.loans:
            loan = self.loans[loan_id]
            print(
                f"Loan {loan_id}: ${loan.amount:.2f} at {loan.interest_rate:.2f}% interest rate")
        else:
            print("Invalid loan ID!")

    @classmethod
    def show_all_loans(self):
        """Shows all loans."""
        if not self.loans:
            print("No loans available.")
            return

        for loan_id, loan in self.loans.items():
            print(
                f"Loan {loan_id}: ${loan.amount:.2f} at {loan.interest_rate:.2f}% interest rate")

    @classmethod
    def generate_report(self):
        """Generates a report for the bank system."""
        print("\n--- Bank System Report ---")

        # Savings Account Report
        print("\nSavings Account:")
        print(f"Balance: ${self.savings.balance:.2f}")

        # Loans Report
        print("\nLoans:")
        if not self.loans:
            print("No loans available.")
        else:
            for loan_id, loan in self.loans.items():
                print(
                    f"Loan {loan_id}: ${loan.amount:.2f} at {loan.interest_rate:.2f}% annual interest rate")

        # Transactions Report
        print("\nTransactions:")
        for transaction in self.transactions:
            print(transaction)

    @classmethod
    def show_help(self):
        """Shows the help menu."""
        print("""
        Commands:
        1. Advance Month
        2. Deposit to Savings
        3. Withdraw from Savings
        4. Create New Loan
        5. Pay Loan
        6. Show Savings Balance
        7. Show Loan
        8. Show All Loans
        9. Generate Report
        10. Help\n
        ----------------
        0. Exit
        """)

    @staticmethod
    def validate_decimal_input(prompt):
        """ Ensures that input is a valid decimal number """
        while True:
            try:
                return Decimal(input(prompt))
            except InvalidOperation:
                print("Invalid input. Please enter a numerical value.")

    @staticmethod
    def validate_int_input(prompt):
        """ Ensures that input is an int"""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    @staticmethod
    def loan_exists(loan_id):
        """ Ensures that the loan id actually exists"""
        return loan_id in [loan.id for loan in BankSystem.loans if hasattr(loan, 'id')]
