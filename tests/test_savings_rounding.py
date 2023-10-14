import unittest
from Banking.BankSystem import BankSystem
from Banking.SavingsAccount import SavingsAccount
from decimal import Decimal
import config 


class TestSavingsRounding(unittest.TestCase):
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

    def test_apply_savings_interest(self):
        # Testing applying savings interest
        initial_balance = Decimal('1000.00')
        interest_rate = Decimal('0.03')

        BankSystem.savings = SavingsAccount(interest_rate)
        BankSystem.savings.balance = initial_balance

        result = BankSystem.savings.apply_interest()

        monthly_interest_rate = interest_rate / Decimal('12')
        expected_interest = (initial_balance * monthly_interest_rate)  
        expected_interest = expected_interest.quantize(Decimal('0.01'))
        expected_balance = initial_balance + expected_interest
        expected_message = f"Applied ${expected_interest} interest. New savings balance: ${expected_balance}"

        self.assertEqual(result, expected_message, f'Expected "{expected_message}" but got "{result}"')
        self.assertEqual(BankSystem.savings.balance, expected_balance, f'Expected balance of "{expected_balance}" but got "{BankSystem.savings.balance}"')

    def test_apply_savings_interest_rounding(self):
        # Interest results in a fraction of a penny
        account1 = SavingsAccount(interest_rate=Decimal('0.12'))  # 12% annual interest
        account1.deposit(Decimal('100'))
        result = account1.apply_interest()
        self.assertEqual(result, "Applied $1.00 interest. New savings balance: $101.00")

        # Validate Rounding down
        account3 = SavingsAccount(interest_rate=Decimal('0.125'))  # 12.5% annual interest
        account3.deposit(Decimal('1')) 
        result = account3.apply_interest()
        self.assertEqual(result, "Applied $0.01 interest. New savings balance: $1.01")

    
if __name__ == '__main__':
    unittest.main()
