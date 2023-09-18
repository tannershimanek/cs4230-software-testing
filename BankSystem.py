from loan import Loan
import math
import config

# note: interest is applied to the loan amount before the late fee is applied


# Receiver
class BankSystem:
    savings_balance = 0
    savings_interest_rate = config.BANK_CONFIG.get('savings_rate')
    loans = {}
    loan_payments = {}  # Track payments for each loan for the current month
    num_loans = 0
    current_month = 1
    transactions = []

    @classmethod
    def advance_month(self):
        """Advances the month by 1, processes interest rates and late fees, and generates a report."""
        self.current_month += 1
        print(f"Advanced to month {self.current_month}\n")

        # Apply late fee to loans without payments
        for loan_id, loan in self.loans.items():
            if loan_id not in self.loan_payments or self.loan_payments[loan_id] == 0:
                loan["amount"] += 50
                self.log_transaction(
                    f"Applied $50 late fee to loan {loan_id}. New balance: ${loan['amount']}")
                print(
                    f"Applied $50 late fee to loan {loan_id}. New balance: ${loan['amount']}")

        self.process_loan_interest()
        self.process_savings_interest()
        self.loan_payments.clear()  # Reset loan payments for the new month
        self.generate_report()

    @classmethod
    def log_transaction(self, description):
        """Logs a transaction to the transactions list for the bank report."""
        self.transactions.append(f"Month {self.current_month}: {description}")

    # @classmethod
    # def create_savings_account(self):
    #     """Creates a new savings account with a balance of 0. [DEPRECATED."""
    #     self.savings_balance = 0
    #     print("[DEPRICATED] Savings account created!")

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
        """Creates a new loan with the given amount and interest rate."""
        loan_id = len(self.loans) + 1
        interest_rate = config.BANK_CONFIG.get('interest_rate')
        # math.ceil(amount*100)/100 rounds up to the nearest cent
        self.loans[loan_id] = {"amount": math.ceil(amount*100)/100,
                               "interest_rate": interest_rate}
        print(
            f"Created new loan with ID {loan_id} for ${amount} at {interest_rate}% interest rate")

    @classmethod
    def pay_loan(self, loan_id, amount):
        """Pays the given amount to the given loan from the savings account."""
        if loan_id in self.loans:
            self.loans[loan_id]["amount"] -= amount
            self.loan_payments[loan_id] = self.loan_payments.get(
                loan_id, 0) + amount
            if self.loans[loan_id]["amount"] < 0.01:
                self.loans[loan_id]["amount"] = 0
                self.loans.pop(loan_id)  # remove loan from loans dict
                self.log_transaction(f"Loan {loan_id} paid off!")
                print(f"Loan {loan_id} paid off!")
            print(
                f"Paid ${amount:.2f} for loan {loan_id}. Remaining amount: ${self.loans[loan_id]['amount']:.2f}")
        else:
            print("Invalid loan ID!")

    @classmethod
    def show_savings_balance(self):
        """Shows the current savings balance."""
        print(f"Savings balance: ${self.savings_balance:.2f}")

    @classmethod
    def show_loan(self, loan_id):
        """Shows the given loan."""
        if loan_id in self.loans:
            print(
                f"Loan {loan_id}: ${self.loans[loan_id]['amount']:.2f} at {self.loans[loan_id]['interest_rate']:.2f}% interest rate")
        else:
            print("Invalid loan ID!")

    @classmethod
    def show_all_loans(self):
        """Shows all loans."""
        for loan_id, loan in self.loans.items():
            print(
                f"Loan {loan_id}: ${loan['amount']:.2f} at {loan['interest_rate']:.2f}% interest rate")

    @classmethod
    def process_loan_interest(self):
        for loan_id, loan in self.loans.items():
            interest = (loan['amount'] * loan['interest_rate']) / 100
            loan['amount'] += math.ceil(interest*100)/100
            self.log_transaction(
                f"Applied ${interest:.2f} interest to loan {loan_id}. New balance: ${loan['amount']:.2f}")
            print(
                f"Applied ${interest:.2f} interest to loan {loan_id}. New balance: ${loan['amount']:.2f}")

    @classmethod
    def process_savings_interest(self):
        interest = (self.savings_balance * self.savings_interest_rate) / 100
        self.savings_balance += interest
        self.log_transaction(
            f"Applied ${interest:.2f} interest to savings. New balance: ${self.savings_balance:.2f}")
        print(
            f"Applied ${interest:.2f} interest to savings. New balance: ${self.savings_balance:.2f}")

    @classmethod
    def generate_report(self):
        """Generates a report for the bank system."""
        print("\n--- Bank System Report ---")
        print("\nSavings Account:")
        print(f"Balance: ${round(self.savings_balance, 2):.2f}")

        print("\nLoans:")
        for loan_id, loan in self.loans.items():
            print(
                f"Loan {loan_id}: ${loan['amount']:.2f} at {loan['interest_rate']}% interest rate")

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
