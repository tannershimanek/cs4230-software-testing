import unittest
import Banking.Commands as Commands
from Banking.BankSystem import BankSystem
# from copy import deepcopy

# python3 -m unittest tests.test_banking


class BankSystemTest(unittest.TestCase):

    def test_pay_loan(self):
        # Initial setup
        initial_deposit = 1000
        loan_amount = 500
        payment_amount = 150

        # Execute commands
        Commands.DepositToSavingsCommand(initial_deposit).execute()
        Commands.CreateNewLoanCommand(loan_amount, 12).execute()
        Commands.PayLoanCommand(1, payment_amount).execute()

        # Check savings balance
        expected_savings_balance = initial_deposit - payment_amount
        self.assertEqual(BankSystem.savings.balance, expected_savings_balance)

        # Check loan amount
        loan = BankSystem.loans[1]
        expected_loan_balance = loan_amount - payment_amount
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
