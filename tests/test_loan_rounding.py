import unittest
from Banking.Loan import Loan
from decimal import Decimal


class TestLoanRounding(unittest.TestCase):

    def setUp(self):
        self.interest_rate = 12

    def test_rounding_loan_amount(self):
        # Test rounding up the loan amount to the nearest penny
        loan = Loan(1000.009, self.interest_rate)
        self.assertEqual(loan.amount, Decimal('1000.01'))

    def test_rounding_payment_amount(self):
        # Test rounding down the amount paid to the loan to the nearest penny
        loan = Loan(1000, self.interest_rate)
        loan.pay(100.009)  # Amount paid
        # Remaining loan amount after payment
        self.assertEqual(loan.amount, Decimal('900.00'))

    def test_rounding_late_fee(self):
        # Test rounding down the loan late fee to the nearest penny
        # Set a decimal late fee for this test
        Loan.late_fee = Decimal('50.009')
        loan = Loan(1000, self.interest_rate)
        loan.apply_late_fee()
        # Loan amount after applying late fee
        self.assertEqual(loan.amount, Decimal('1050.00'))

    def test_rounding_interest(self):
        # Test rounding up the interest applied to a loan to the nearest penny
        loan = Loan(1000, self.interest_rate)
        interest = loan.apply_interest()
        # Monthly interest on $1000 at 12% yearly rate
        self.assertEqual(interest, Decimal('10.00'))


if __name__ == '__main__':
    unittest.main()
