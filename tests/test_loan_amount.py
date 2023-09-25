import unittest
from Banking.Loan import Loan

class TestLoanInitialization(unittest.TestCase):

    def test_positive_amount(self):
        loan = Loan(5000, 12)
        self.assertEqual(loan.amount, 5000)
        self.assertEqual(loan.interest_rate, 12)

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            Loan(0,12)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):  # Assuming a ValueError is raised for negative amounts
            Loan(-5000, 12)

if __name__ == "__main__":
    unittest.main()
