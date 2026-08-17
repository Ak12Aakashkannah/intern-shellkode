# Bank Account Class

class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit money
    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount

        print(f"{self.account_holder} deposited ₹{amount}")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount

        print(f"{self.account_holder} withdrew ₹{amount}")

    # Display account details
    def display_balance(self):

        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance}")


# Savings Account

class SavingsAccount(BankAccount):

    def __init__(self, account_holder, balance=0, interest_rate=5):

        super().__init__(account_holder, balance)

        self.interest_rate = interest_rate

    # Add interest
    def add_interest(self):

        interest = self.balance * self.interest_rate / 100

        self.balance += interest

        print(f"Interest added: ₹{interest:.2f}")


# Current Account

class CurrentAccount(BankAccount):

    def __init__(self, account_holder, balance=0, overdraft_limit=0):

        super().__init__(account_holder, balance)

        self.overdraft_limit = overdraft_limit

    # Withdraw with overdraft
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        available_money = self.balance + self.overdraft_limit

        if amount > available_money:
            raise ValueError("Overdraft limit exceeded.")

        self.balance -= amount

        print(f"{self.account_holder} withdrew ₹{amount}")


# Create Accounts

account1 = BankAccount("Rahul", 10000)

account2 = SavingsAccount("Priya", 20000, 5)

account3 = CurrentAccount("Amit", 5000, 3000)


# Test Bank Account

print("ACCOUNT 1")
print("---------")

account1.display_balance()

account1.deposit(2000)

account1.withdraw(1000)

account1.display_balance()


# Test Savings Account

print()
print("ACCOUNT 2 - SAVINGS")
print("-------------------")

account2.display_balance()

account2.deposit(5000)

account2.add_interest()

account2.display_balance()


# Test Current Account

print()
print("ACCOUNT 3 - CURRENT")
print("-------------------")

account3.display_balance()

account3.withdraw(7000)

account3.display_balance()


# Transfer Money

def transfer_money(sender, receiver, amount):

    if amount <= 0:
        raise ValueError("Transfer amount must be positive.")

    # Withdraw from sender
    sender.withdraw(amount)

    # Deposit into receiver
    receiver.deposit(amount)

    print()
    print(f"₹{amount} transferred successfully.")
    print(f"From: {sender.account_holder}")
    print(f"To: {receiver.account_holder}")


# Test Transfer

print()
print("TRANSFER")
print("--------")

print("Before transfer:")

account1.display_balance()
account2.display_balance()

transfer_money(account1, account2, 2000)

print()
print("After transfer:")

account1.display_balance()
account2.display_balance()