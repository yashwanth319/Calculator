class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self.balance -= amount
        print(f"Withdrawn: ${amount}. New balance: ${self.balance}")

# Example usage
try:
    account = BankAccount()
    account.deposit(100)
    account.withdraw(150)  # This should raise InsufficientFundsError
except ValueError as ve:
    print(f"ValueError: {ve}")
except InsufficientFundsError as ife:
    print(f"InsufficientFundsError: {ife}")
