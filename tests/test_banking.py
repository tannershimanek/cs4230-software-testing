import unittest
from Banking.Loan import Loan
from Banking.SavingsAccount import SavingsAccount
import Banking.Commands as Commands
from Banking.BankSystem import BankSystem
# from copy import deepcopy

# python3 -m unittest tests.test_banking


class BankSystemTest(unittest.TestCase):

    def setUp(self) -> None:
        self.savings = SavingsAccount(3)
        self.initial_deposit = 1000
        self.negative_amount = -100
        self.zero_amount = 0
        self.billion = 1000000000
        self.loan_amount = 500
        self.payment_amount = 150

    def test_create_savings(self):
        self.assertEqual(self.savings.interest_rate, 3)

    def test_valid_initial_deposit_savings(self):
        self.savings.deposit(self.initial_deposit)
        self.assertEqual(self.savings.balance, self.initial_deposit)

    def test_negative_deposit_savings(self):
        self.savings.deposit(self.negative_amount)
        self.assertEqual(self.savings.balance, 0)

    def test_zero_deposit_savings(self):
        self.savings.deposit(self.zero_amount)
        self.assertEqual(self.savings.balance, 0)

    def test_too_large_deposit_savings(self):
        self.savings.deposit(self.billion)
        self.assertEqual(self.savings.balance, 0)

    def test_invalid_deposit_savings(self) -> None:
        with self.assertRaises(TypeError):
            self.savings.deposit('abc')

    def test_withdrawl_valid_data(self):
        self.savings.deposit(self.initial_deposit)
        self.savings.withdraw(100)
        self.assertEqual(self.savings.balance, 900)

    def test_withdrawl_invalid_data(self):
        self.savings.deposit(self.initial_deposit)
        with self.assertRaises(TypeError):
            self.savings.withdraw('abc')
    
    def test_withdrawl_more_than_balance(self):
        self.savings.deposit(self.initial_deposit)
        self.savings.withdraw(10000)
        self.assertEqual(self.savings.balance, self.initial_deposit)

    def test_withdrawl_zero(self):
        self.savings.deposit(self.initial_deposit)
        self.savings.withdraw(self.zero_amount)
        self.assertEqual(self.savings.balance, self.initial_deposit)
        
    def test_withdrawl_multiple(self):
        self.savings.deposit(self.initial_deposit)
        self.savings.withdraw(100)
        self.savings.withdraw(50)
        self.savings.withdraw(25)
        self.savings.withdraw(75)
        self.assertEqual(self.savings.balance, 750)

    def test_pay_loan(self):

        # Execute commands
        Commands.DepositToSavingsCommand(self.initial_deposit).execute()
        Commands.CreateNewLoanCommand(self.loan_amount, 12).execute()
        Commands.PayLoanCommand(1, self.payment_amount).execute()

        # Check savings balance
        expected_savings_balance = self.initial_deposit - self.payment_amount
        self.assertEqual(BankSystem.savings.balance, expected_savings_balance)

        # Check loan amount
        loan = BankSystem.loans[1]
        expected_loan_balance = self.loan_amount - self.payment_amount
        self.assertEqual(loan.amount, expected_loan_balance)

    # def test_loan_interest(self):
    #     # Initial setup
    #     initial_deposit = 1000
    #     loan_amount = 500
    #     payment_amount = 150
    #     interest_rate = 0.01
    #     BS = BankSystem()

    #     # Execute commands
    #     Commands.DepositToSavingsCommand(initial_deposit).execute()
    #     Commands.CreateNewLoanCommand(loan_amount, 12).execute()
    #     Commands.PayLoanCommand(1, payment_amount).execute()
    #     Commands.AdvanceMonthCommand().execute()

    #     # Check savings balance
    #     # expected_savings_balance = initial_deposit - payment_amount
    #     # self.assertEqual(BankSystem.savings.balance, expected_savings_balance)

    #     # Check loan amount
    #     loan = BS.loans[1]
    #     expected_interest = (loan_amount - payment_amount) * interest_rate
    #     expected_loan_balance = loan_amount - payment_amount + expected_interest
    #     self.assertEqual(loan.amount, expected_loan_balance)

    #     # # Check loan interest
    #     # expected_loan_balance = expected_loan_balance * 1.01
    #     # self.assertEqual(loan.amount, expected_loan_balance)


if __name__ == '__main__':
    unittest.main()
