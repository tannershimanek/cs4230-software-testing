import unittest

class ValidSavingsAccount:
    def __init__(self, interest_rate):
        self.balance = 0

        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Invalid interest rate. It should be a positive real number.")
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid deposit amount. It should be a real number.")

        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")

        self.balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid withdrawal amount. It should be a real number.")

        if amount < 0:
            raise ValueError("Withdrawal amount may not be negative.")

        if amount > self.balance:
            raise ValueError("Insufficient funds!")

        self.balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

    # The apply_interest method remains the same as there's no specific rule given for this action.

    def apply_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        return f"Applied ${interest:.2f} interest. New savings balance: ${self.balance:.2f}"

class TestValidSavingsAccount(unittest.TestCase):

    def test_valid_interest_rate(self):
        acc = ValidSavingsAccount(5)
        self.assertEqual(acc.interest_rate, 5)

    def test_invalid_interest_rate(self):
        with self.assertRaises(ValueError):
            ValidSavingsAccount(-5)

    def test_valid_deposit_positive_amount(self):
        acc = ValidSavingsAccount(5)
        result = acc.deposit(100)
        self.assertEqual(result, "Deposited $100.00. New balance: $100.00")

    def test_valid_deposit_zero_amount(self):
        acc = ValidSavingsAccount(5)
        result = acc.deposit(0)
        self.assertEqual(result, "Deposited $0.00. New balance: $0.00")

    def test_invalid_deposit_negative_amount(self):
        acc = ValidSavingsAccount(5)
        with self.assertRaises(ValueError):
            acc.deposit(-50)

    def test_valid_withdrawal(self):
        acc = ValidSavingsAccount(5)
        acc.deposit(100)
        result = acc.withdraw(50)
        self.assertEqual(result, "Withdrew $50.00. New balance: $50.00")

    def test_invalid_withdrawal_negative(self):
        acc = ValidSavingsAccount(5)
        with self.assertRaises(ValueError):
            acc.withdraw(-50)

    def test_invalid_withdrawal_excess(self):
        acc = ValidSavingsAccount(5)
        acc.deposit(100)
        with self.assertRaises(ValueError):
            acc.withdraw(150)

    def test_balance_after_deposit(self):
        acc = ValidSavingsAccount(5)
        acc.deposit(50)
        self.assertEqual(acc.balance, 50)

    def test_balance_after_withdrawal(self):
        acc = ValidSavingsAccount(5)
        acc.deposit(100)
        acc.withdraw(50)
        self.assertEqual(acc.balance, 50)

    def test_balance_negative_after_deposit(self):
        acc = ValidSavingsAccount(5)
        with self.assertRaises(ValueError):
            acc.deposit(-50)

    def test_balance_negative_after_withdrawal(self):
        acc = ValidSavingsAccount(5)
        acc.deposit(100)
        with self.assertRaises(ValueError):
            acc.withdraw(150)

if __name__ == "__main__":
    unittest.main()
