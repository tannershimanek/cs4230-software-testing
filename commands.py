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


# Receiver
# class BankSystem:
#     # fixme: this should be updated with other group members classes
#     savings_balance = 0
#     loans = {}
#     num_loans = 0
#     current_month = 1
#     transactions = []

#     @classmethod
#     def advance_month(cls):
#         cls.current_month += 1
#         print(f"Advanced to month {cls.current_month}")

#     @classmethod
#     def log_transaction(cls, description):
#         cls.transactions.append(f"Month {cls.current_month}: {description}")

#     @classmethod
#     def create_savings_account(cls):
#         cls.savings_balance = 0
#         print("Savings account created!")

#     @classmethod
#     def deposit_to_savings(cls, amount):
#         cls.savings_balance += amount
#         cls.log_transaction(f"Deposited ${amount} to savings. New balance: ${cls.savings_balance}")
#         print(f"Deposited ${amount} to savings. New balance: ${cls.savings_balance}")

#     @classmethod
#     def withdraw_from_savings(cls, amount):
#         if amount <= cls.savings_balance:
#             cls.savings_balance -= amount
#             cls.log_transaction(f"Withdrew ${amount} from savings. New balance: ${cls.savings_balance}")
#             print(f"Withdrew ${amount} from savings. New balance: ${cls.savings_balance}")
#         else:
#             print("Insufficient funds!")

#     @classmethod
#     def create_new_loan(cls, amount, interest_rate):
#         loan_id = len(cls.loans) + 1
#         cls.loans[loan_id] = {"amount": amount, "interest_rate": interest_rate}
#         print(
#             f"Created new loan with ID {loan_id} for ${amount} at {interest_rate}% interest rate")

#     @classmethod
#     def pay_loan(cls, loan_id, amount):
#         if loan_id in cls.loans:
#             cls.loans[loan_id]["amount"] -= amount
#             print(
#                 f"Paid ${amount} for loan {loan_id}. Remaining amount: ${cls.loans[loan_id]['amount']}")
#         else:
#             print("Invalid loan ID!")

#     @classmethod
#     def show_savings_balance(cls):
#         print(f"Savings balance: ${cls.savings_balance}")

#     @classmethod
#     def show_loan(cls, loan_id):
#         if loan_id in cls.loans:
#             print(
#                 f"Loan {loan_id}: ${cls.loans[loan_id]['amount']} at {cls.loans[loan_id]['interest_rate']}% interest rate")
#         else:
#             print("Invalid loan ID!")

#     @classmethod
#     def show_all_loans(cls):
#         for loan_id, loan in cls.loans.items():
#             print(
#                 f"Loan {loan_id}: ${loan['amount']} at {loan['interest_rate']}% interest rate")

#     @classmethod
#     def generate_report(cls):
#         print("\n--- Bank System Report ---")
#         print("\nSavings Account:")
#         print(f"Balance: ${cls.savings_balance}")

#         print("\nLoans:")
#         for loan_id, loan in cls.loans.items():
#             print(f"Loan {loan_id}: ${loan['amount']} at {loan['interest_rate']}% interest rate")

#         print("\nTransactions:")
#         for transaction in cls.transactions:
#             print(transaction)

#     @classmethod
#     def show_help(cls):
#         print("""
#         Commands:
#         1. Advance Month
#         2. Deposit to Savings
#         3. Withdraw from Savings
#         4. Create New Loan
#         5. Pay Loan
#         6. Show Savings Balance
#         7. Show Loan
#         8. Show All Loans
#         9. Generate Report
#         10. Help\n
#         ----------------
#         0. Exit
#         """)

# def driver():
#     while True:
#         command = input("\nEnter your command (type 'help' for available commands): ").lower().strip()

#         if command == "advance_month" or command == "1":
#             cmd = AdvanceMonthCommand()
#         elif command == "deposit_to_savings" or command == "2":
#             amount = float(input("Enter amount to deposit: "))
#             cmd = DepositToSavingsCommand(amount)
#         elif command == "withdraw_from_savings" or command == "3":
#             amount = float(input("Enter amount to withdraw: "))
#             cmd = WithdrawFromSavingsCommand(amount)
#         elif command == "create_new_loan" or command == "4":
#             amount = float(input("Enter loan amount: "))
#             interest_rate = float(input("Enter interest rate: "))
#             cmd = CreateNewLoanCommand(amount, interest_rate)
#         elif command == "pay_loan" or command == "5":
#             loan_id = int(input("Enter loan ID: "))
#             amount = float(input("Enter amount to pay: "))
#             cmd = PayLoanCommand(loan_id, amount)
#         elif command == "show_savings_balance" or command == "6":
#             cmd = ShowSavingsBalanceCommand()
#         elif command == "show_loan" or command == "7":
#             loan_id = int(input("Enter loan ID: "))
#             cmd = ShowLoanCommand(loan_id)
#         elif command == "show_all_loans" or command == "8":
#             cmd = ShowAllLoansCommand()
#         elif command == "generate_report" or command == "9":
#             cmd = GenerateReportCommand()
#         elif command == "help" or command == "10":
#             cmd = HelpCommand()
#         elif command == "exit" or command == "0":
#             print("Exiting the system. Goodbye!")
#             break
#         else:
#             print("Invalid command. Type 'help' for available commands.")
#             continue

#         cmd.execute()

# if __name__ == "__main__":
#     driver()


# # Client
# if __name__ == "__main__":
#     # This is just a simple demonstration. In a real-world application, you'd probably have a more sophisticated client interface.
#     cmd = HelpCommand()
#     cmd.execute()
