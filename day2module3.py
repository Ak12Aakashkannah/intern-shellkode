import csv
import json


# Create Dummy CSV File

students = [
    ["Name", "Grade"],
    ["Rahul", 85],
    ["Priya", 92],
    ["Amit", 78],
    ["Sneha", 88],
    ["Karan", 95]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(students)

print("students.csv created successfully.")


# Read CSV File

grades = []

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        grade = float(row["Grade"])

        grades.append(grade)


# Calculate Average

average_grade = sum(grades) / len(grades)

print()
print("Student Grades:")
print(grades)

print()
print(f"Average Grade: {average_grade:.2f}")


# Create JSON Summary

summary = {
    "total_students": len(grades),
    "average_grade": average_grade,
    "highest_grade": max(grades),
    "lowest_grade": min(grades)
}

with open("summary.json", "w") as file:

    json.dump(summary, file, indent=4)

print()
print("summary.json created successfully.")


# Read JSON File

with open("summary.json", "r") as file:

    data = json.load(file)

print()
print("JSON SUMMARY")
print("------------")

print("Total Students:", data["total_students"])
print("Average Grade:", data["average_grade"])
print("Highest Grade:", data["highest_grade"])
print("Lowest Grade:", data["lowest_grade"])


# Custom Exception

class InsufficientFundsError(Exception):

    def __init__(self, message="Insufficient funds."):
        self.message = message
        super().__init__(self.message)


# Bank Account with Error Handling

class SafeBankAccount:

    def __init__(self, account_holder, balance=0):

        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_holder = account_holder
        self.balance = balance

    # Deposit money
    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount

        print(f"₹{amount} deposited successfully.")

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance.")

        self.balance -= amount

        print(f"₹{amount} withdrawn successfully.")

    # Display balance
    def display_balance(self):

        print(
            f"{self.account_holder}'s balance: "
            f"₹{self.balance}"
        )


# Test Error Handling

print()
print("ERROR HANDLING")
print("--------------")

account = SafeBankAccount("Aakash", 10000)

account.display_balance()


# Valid deposit
try:

    account.deposit(2000)

except ValueError as e:

    print("Error:", e)


# Invalid negative deposit
try:

    account.deposit(-500)

except ValueError as e:

    print("Error:", e)


# Valid withdrawal
try:

    account.withdraw(3000)

except InsufficientFundsError as e:

    print("Error:", e)


# Withdrawal greater than balance
try:

    account.withdraw(20000)

except InsufficientFundsError as e:

    print("Error:", e)


account.display_balance()


# Current Account with Custom Exception

class SafeCurrentAccount(SafeBankAccount):

    def __init__(
        self,
        account_holder,
        balance=0,
        overdraft_limit=0
    ):

        super().__init__(account_holder, balance)

        if overdraft_limit < 0:
            raise ValueError(
                "Overdraft limit cannot be negative."
            )

        self.overdraft_limit = overdraft_limit

    # Withdraw money with overdraft
    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be positive."
            )

        available_money = self.balance + self.overdraft_limit

        if amount > available_money:

            raise InsufficientFundsError(
                "Withdrawal exceeds overdraft limit."
            )

        self.balance -= amount

        print(f"₹{amount} withdrawn successfully.")


# Test Current Account

print()
print("CURRENT ACCOUNT")
print("---------------")

current = SafeCurrentAccount(
    "Aakash",
    5000,
    3000
)

current.display_balance()


# Withdrawal using overdraft
try:

    current.withdraw(7000)

except InsufficientFundsError as e:

    print("Error:", e)


current.display_balance()


# Withdrawal exceeding overdraft limit
try:

    current.withdraw(9000)

except InsufficientFundsError as e:

    print("Error:", e)


current.display_balance()