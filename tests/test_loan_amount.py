import unittest
import random
from Banking.Loan import Loan
from decimal import InvalidOperation

class TestLoanInitialization(unittest.TestCase):

    def test_random_positive_amount_within_range(self) -> None:
        random_amount = random.randint(500, 50000)
        loan = Loan(random_amount, 12)
        self.assertTrue(500 <= loan.amount <= 50000, f"Loan amount {loan.amount} is outside the allowed range")
        self.assertEqual(loan.amount, random_amount)
        self.assertEqual(loan.interest_rate, 12)

    def test_zero_amount(self) -> None:
        with self.assertRaises(ValueError):
            Loan(0,12)

    def test_negative_amount(self) -> None:
        with self.assertRaises(ValueError):
            Loan(-5000, 12)

    def test_is_number(self) -> None:
        with self.assertRaises(InvalidOperation):
            Loan('abc', 12)

if __name__ == "__main__":
    unittest.main()
