import unittest
from Banking.Loan import Loan

class TestLateFee(unittest.TestCase):

    def test_payment_this_month(self) -> None: 
        loan = Loan(5000, 12)
        minimum_payment = loan.calculate_minimum_payment()
        loan.pay(150)
        self.assertGreaterEqual(loan.payment_this_month, minimum_payment)

if __name__ == "__main__":
    unittest.main()
