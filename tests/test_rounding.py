import unittest
from Banking.BankSystem import BankSystem
from Banking.SavingsAccount import SavingsAccount
from decimal import Decimal
import config 

class TestRounding(unittest.TestCase):
    def setUp(self):
        BankSystem.savings = SavingsAccount(config.BANK_CONFIG.get('savings_rate'))
        BankSystem.loans = {}
        BankSystem.num_loans = 0
        BankSystem.current_loan_number = 0
        BankSystem.current_month = 1
        BankSystem.transactions = []

    def test_deposit_rounding(self):
        # Test rounding to the nearest penny on account deposits
        BankSystem.savings.deposit(50.099)
        self.assertEqual(BankSystem.savings.balance, Decimal('50.09'), "Deposit rounding failed")
        
    def test_withdraw_rounding(self):
        # Test rounding to the nearest penny on account withdrawals 
        BankSystem.savings.deposit(100.00)
        BankSystem.savings.withdraw(50.095)
        self.assertEqual(BankSystem.savings.balance, Decimal('49.91'), "Withdraw rounding failed")


if __name__ == '__main__':
    unittest.main()
