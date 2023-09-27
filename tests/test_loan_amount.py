import unittest
from Banking.Loan import Loan

class TestLoanInitialization(unittest.TestCase):

    def test_positive_amount(self) -> None:
        loan = Loan(5000, 12)
        self.assertEqual(loan.amount, 5000)
        self.assertEqual(loan.interest_rate, 12)

    def test_zero_amount(self) -> None:
        with self.assertRaises(ValueError):
            Loan(0,12)

    def test_negative_amount(self) -> None:
        with self.assertRaises(ValueError):
            Loan(-5000, 12)

    def test_is_number(self) -> None:
        with self.assertRaises(TypeError):
            Loan('abc', 12)

if __name__ == "__main__":
    unittest.main()
