import unittest
from Banking.Loan import Loan
from decimal import InvalidOperation


class TestInterestRate(unittest.TestCase):

    def test_positive_interest(self) -> None:
        loan = Loan(5000, 12)
        self.assertEqual(loan.interest_rate, 12)

    def test_upper_boundary(self) -> None:
        loan = Loan(5000, 18)
        self.assertEqual(loan.interest_rate, 18)

    def test_lower_boundary(self) -> None:
        loan = Loan(5000, 1)
        self.assertEqual(loan.interest_rate, 1)

    def test_zero_rate(self) -> None:
        with self.assertRaises(ValueError):
            Loan(5000, 0)

    def test_negative_rate(self) -> None:
        with self.assertRaises(ValueError):
            Loan(5000, -1)

    def test_more_than_18(self) -> None:
        with self.assertRaises(ValueError):
            Loan(5000, 19)

    def test_is_number(self) -> None:
        with self.assertRaises(InvalidOperation):
            Loan(5000, 'abc')


if __name__ == "__main__":
    unittest.main()
