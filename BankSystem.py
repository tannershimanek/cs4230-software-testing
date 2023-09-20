from Loan import Loan
import math
import config

# note: interest is applied to the loan amount before the late fee is applied

"""
todo:
    - set minimum loan payment (interest due + 1% of loan amount + late fee (if applicable) or $10. Whichever is greater.)
    - savings cannot be negative
    - loan payment comes from savings
    - loan payment cannot be greater than savings amount
    - change interest rate from 12% to 1% of loan amount each month.
    - change savings interest rate 3% to 1% of savings amount each month.

"""

# Receiver


class BankSystem:
    savings_balance = 0
    savings_interest_rate = config.BANK_CONFIG.get('savings_rate')
    loans = {}
    num_loans = 0
    current_month = 1
    transactions = []

    @classmethod
    def advance_month(self):
        self.current_month += 1
        print(f"Advanced to month {self.current_month}\n")

        for loan_id, loan in self.loans.items():
            if loan.payment_this_month == 0:
                loan.apply_late_fee()
                self.log_transaction(
                    f"Applied $50 late fee to loan {loan_id}. New balance: ${loan.amount}")
                print(
                    f"Applied $50 late fee to loan {loan_id}. New balance: ${loan.amount}")

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
        """Deposits the given amount to the savings account."""
        self.savings_balance += math.floor(amount*100) / \
            100  # rounds down to the nearest cent
        self.log_transaction(
            f"Deposited ${amount} to savings. New balance: ${self.savings_balance}")
        print(
            f"Deposited ${amount} to savings. New balance: ${self.savings_balance}")

    @classmethod
    def withdraw_from_savings(self, amount):
        """Withdraws the given amount from the savings account."""
        if amount <= self.savings_balance:
            self.savings_balance -= amount
            self.savings_balance = round(self.savings_balance, 2)
            self.log_transaction(
                f"Withdrew ${amount} from savings. New balance: ${self.savings_balance}")
            print(
                f"Withdrew ${amount} from savings. New balance: ${self.savings_balance}")
        else:
            print("Insufficient funds!")

    @classmethod
    def create_new_loan(self, amount, interest_rate):
        if len(self.loans) >= 3:
            print("Maximum number of loans reached. Cannot create a new loan.")
            return

        if 500 <= amount <= 50000:
            loan_id = len(self.loans) + 1
            self.loans[loan_id] = Loan(amount, interest_rate)
            print(
                f"Created new loan with ID {loan_id} for ${amount} at {interest_rate}% interest rate")
        else:
            print(
                "Loan amount is invalid. Please ensure amount is between $500 and $50,000.")

    @classmethod
    def pay_loan(self, loan_id, amount):
        if loan_id in self.loans:
            loan = self.loans[loan_id]
            min_payment = loan.calculate_minimum_payment()
            if amount < min_payment:
                print(
                    f"Payment is below the minimum required amount of ${min_payment:.2f}. Payment not processed.")
                return

            if amount > loan.amount:
                print(
                    f"Payment is greater than the loan amount. Please pay an amount up to ${loan.amount:.2f}.")
                return

            loan.pay(amount)
            self.log_transaction(
                f"Paid ${amount:.2f} for loan {loan_id}. Remaining amount: ${loan.amount:.2f}")

            if loan.amount < 0.01:
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
        for loan_id, loan in self.loans.items():
            interest = loan.apply_interest()
            self.log_transaction(
                f"Applied ${interest:.2f} interest to loan {loan_id}. New balance: ${loan.amount:.2f}")
            print(
                f"Applied ${interest:.2f} interest to loan {loan_id}. New balance: ${loan.amount:.2f}")

    @classmethod
    def show_savings_balance(self):
        """Shows the current savings balance."""
        print(f"Savings balance: ${self.savings_balance:.2f}")

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
    def process_savings_interest(self):
        interest = (self.savings_balance *
                    (self.savings_interest_rate / 12)) / 100
        self.savings_balance += interest
        self.log_transaction(
            f"Applied ${interest:.2f} interest to savings. New balance: ${self.savings_balance:.2f}")
        print(
            f"Applied ${interest:.2f} interest to savings. New balance: ${self.savings_balance:.2f}")

    @classmethod
    def generate_report(cls):
        """Generates a report for the bank system."""
        print("\n--- Bank System Report ---")
        print("\nSavings Account:")
        print(f"Balance: ${round(cls.savings_balance, 2):.2f}")

        print("\nLoans:")
        if not cls.loans:
            print("No loans available.")
        else:
            for loan_id, loan in cls.loans.items():
                print(
                    f"Loan {loan_id}: ${loan.amount:.2f} at {loan.interest_rate:.2f}% interest rate")

        print("\nTransactions:")
        for transaction in cls.transactions:
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
