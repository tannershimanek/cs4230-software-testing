from loan import Loan
import config

# todo:
# 1. Create a new loan


# Receiver
class BankSystem:
    # fixme: this should be updated with other group members classes
    savings_balance = 0
    loans = {}
    num_loans = 0
    current_month = 1
    transactions = []

    @classmethod
    def advance_month(cls):
        cls.current_month += 1
        print(f"Advanced to month {cls.current_month}")

    @classmethod
    def log_transaction(cls, description):
        cls.transactions.append(f"Month {cls.current_month}: {description}")

    @classmethod
    def create_savings_account(cls):
        cls.savings_balance = 0
        print("Savings account created!")

    @classmethod
    def deposit_to_savings(cls, amount):
        cls.savings_balance += amount
        cls.log_transaction(f"Deposited ${amount} to savings. New balance: ${cls.savings_balance}")
        print(f"Deposited ${amount} to savings. New balance: ${cls.savings_balance}")

    @classmethod
    def withdraw_from_savings(cls, amount):
        if amount <= cls.savings_balance:
            cls.savings_balance -= amount
            cls.log_transaction(f"Withdrew ${amount} from savings. New balance: ${cls.savings_balance}")
            print(f"Withdrew ${amount} from savings. New balance: ${cls.savings_balance}")
        else:
            print("Insufficient funds!")

    @classmethod
    def create_new_loan(cls, amount, interest_rate):
        loan_id = len(cls.loans) + 1
        interest_rate = config.BANK_CONFIG.get('interest_rate')
        # Loan(loan_id, amount, interest_rate)
        cls.loans[loan_id] = {"amount": amount, "interest_rate": interest_rate}
        print(
            f"Created new loan with ID {loan_id} for ${amount} at {interest_rate}% interest rate")

    @classmethod
    def pay_loan(cls, loan_id, amount):
        if loan_id in cls.loans:
            cls.loans[loan_id]["amount"] -= amount
            print(
                f"Paid ${amount} for loan {loan_id}. Remaining amount: ${cls.loans[loan_id]['amount']}")
        else:
            print("Invalid loan ID!")

    @classmethod
    def show_savings_balance(cls):
        print(f"Savings balance: ${cls.savings_balance}")

    @classmethod
    def show_loan(cls, loan_id):
        if loan_id in cls.loans:
            print(
                f"Loan {loan_id}: ${cls.loans[loan_id]['amount']} at {cls.loans[loan_id]['interest_rate']}% interest rate")
        else:
            print("Invalid loan ID!")

    @classmethod
    def show_all_loans(cls):
        for loan_id, loan in cls.loans.items():
            print(
                f"Loan {loan_id}: ${loan['amount']} at {loan['interest_rate']}% interest rate")

    @classmethod
    def generate_report(cls):
        print("\n--- Bank System Report ---")
        print("\nSavings Account:")
        print(f"Balance: ${cls.savings_balance}")

        print("\nLoans:")
        for loan_id, loan in cls.loans.items():
            print(f"Loan {loan_id}: ${loan['amount']} at {loan['interest_rate']}% interest rate")

        print("\nTransactions:")
        for transaction in cls.transactions:
            print(transaction)

    @classmethod
    def show_help(cls):
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