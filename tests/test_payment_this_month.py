import unittest
from Banking.Loan import Loan


class TestLateFee(unittest.TestCase):

    def test_payment_this_month(self) -> None:
        loan = Loan(5000, 12)
        minimum_payment = loan.calculate_minimum_payment()
        loan.pay(150)
        self.assertGreaterEqual(loan.payment_this_month, minimum_payment)


class TestLoanPayment(unittest.TestCase):
    # test for payment equal to loan amount
    def test_payment_equal_to_loan_amount(self) -> None:
        loan = Loan(5000, 12)
        loan.pay(5000)
        self.assertEqual(loan.payment_this_month, 5000)

    # test for payment greater than loan amount
    def test_payment_greater_than_loan_amount(self) -> None:
        loan = Loan(5000, 12)
        with self.assertRaises(ValueError):
            loan.pay(5000 + 1)

    # test for payment less than loan amount
    def test_payment_less_than_loan_amount(self) -> None:
        loan = Loan(5000, 12)
        loan.pay(5000 - 1)
        self.assertLessEqual(loan.payment_this_month, 5000)

    def test_payment_lower_boundary(self) -> None:
        loan = Loan(5000, 12)
        loan.pay(1)
        self.assertLessEqual(loan.payment_this_month, 5000)

    # test for payment equal to zero
    def test_payment_equal_to_zero(self) -> None:
        loan = Loan(5000, 12)
        with self.assertRaises(ValueError):
            loan.pay(0)

    # test for negative payment_this_month
    def test_negative_payment_this_month(self) -> None:
        loan = Loan(5000, 12)
        with self.assertRaises(ValueError):
            loan.pay(-1)

    # test for payment less than minimum_payment
    def test_payment_less_than_minimum_payment(self) -> None:
        loan = Loan(5000, 12)
        minimum_payment = loan.calculate_minimum_payment()
        loan.apply_late_fee()
        self.assertGreater(loan.amount, 5000 - minimum_payment)

    # test for payment equal to minimum_payment
    def test_payment_equal_to_minimum_payment(self) -> None:
        loan = Loan(5000, 12)
        minimum_payment = loan.calculate_minimum_payment()
        loan.pay(minimum_payment)
        self.assertEqual(loan.amount, 5000 - minimum_payment)

    # test for payment greater than minimum_payment
    def test_payment_greater_than_minimum_payment(self) -> None:
        loan = Loan(5000, 12)
        minimum_payment = loan.calculate_minimum_payment()
        loan.pay(minimum_payment + 1)
        self.assertGreaterEqual(loan.payment_this_month, minimum_payment)


if __name__ == "__main__":
    unittest.main()
