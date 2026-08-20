import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("company.db")

print("Database connected successfully!")

# Create a cursor
cursor = connection.cursor()

# Remove old tables so the program can be run multiple times
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS users")

# Create the users table
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")

connection.commit()

print("Users table created successfully!")

# Insert users into the users table
cursor.executemany("""
INSERT INTO users (name, email)
VALUES (?, ?)
""", [
    ("Aakash", "aakash@example.com"),
    ("Rahul", "rahul@example.com"),
    ("Priya", "priya@example.com"),
    ("Sneha", "sneha@example.com")
])

connection.commit()

print("Users inserted successfully!")

# Create the orders table
cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

connection.commit()

print("Orders table created successfully!")

# Insert orders into the orders table
cursor.executemany("""
INSERT INTO orders (user_id, product, amount)
VALUES (?, ?, ?)
""", [
    (1, "Laptop", 75000),
    (1, "Mouse", 1500),
    (2, "Keyboard", 3000),
    (2, "Headphones", 5000),
    (3, "Monitor", 12000),
    (3, "Webcam", 4000),
    (4, "Keyboard", 3000)
])

connection.commit()

print("Orders inserted successfully!")

# Query 1: SELECT
# Get all users
cursor.execute("""
SELECT *
FROM users
""")

result = cursor.fetchall()

print("\nQuery 1 - All Users:")

for row in result:
    print(row)

# Query 2: WHERE
# Find a specific user
cursor.execute("""
SELECT *
FROM users
WHERE name = ?
""", ("Aakash",))

result = cursor.fetchall()

print("\nQuery 2 - Find Aakash:")

for row in result:
    print(row)

# Query 3: ORDER BY
# Sort users alphabetically by name
cursor.execute("""
SELECT *
FROM users
ORDER BY name ASC
""")

result = cursor.fetchall()

print("\nQuery 3 - Users Sorted by Name:")

for row in result:
    print(row)

# Query 4: GROUP BY and COUNT
# Count the number of orders for each user
cursor.execute("""
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
""")

result = cursor.fetchall()

print("\nQuery 4 - Orders Per User:")

for row in result:
    print(row)

# Query 5: GROUP BY and SUM
# Calculate the total amount spent by each user
cursor.execute("""
SELECT user_id, SUM(amount) AS total_spent
FROM orders
GROUP BY user_id
""")

result = cursor.fetchall()

print("\nQuery 5 - Total Spending Per User:")

for row in result:
    print(row)

# Query 6: AVG
# Calculate the average order amount
cursor.execute("""
SELECT AVG(amount) AS average_order
FROM orders
""")

result = cursor.fetchall()

print("\nQuery 6 - Average Order Amount:")

for row in result:
    print(row)

# Query 7: MIN and MAX
# Find the cheapest and most expensive orders
cursor.execute("""
SELECT
    MIN(amount) AS cheapest_order,
    MAX(amount) AS most_expensive_order
FROM orders
""")

result = cursor.fetchall()

print("\nQuery 7 - Price Range:")

for row in result:
    print(row)

# Query 8: WHERE
# Find orders with an amount greater than 5000
cursor.execute("""
SELECT *
FROM orders
WHERE amount > ?
""", (5000,))

result = cursor.fetchall()

print("\nQuery 8 - Orders Above 5000:")

for row in result:
    print(row)

# Query 9: GROUP BY and HAVING
# Find users whose total spending is greater than 10000
cursor.execute("""
SELECT user_id, SUM(amount) AS total_spent
FROM orders
GROUP BY user_id
HAVING SUM(amount) > 10000
""")

result = cursor.fetchall()

print("\nQuery 9 - Users Spending More Than 10000:")

for row in result:
    print(row)

# Query 10: ORDER BY DESC
# Sort orders from highest amount to lowest amount
cursor.execute("""
SELECT *
FROM orders
ORDER BY amount DESC
""")

result = cursor.fetchall()

print("\nQuery 10 - Orders From Highest to Lowest:")

for row in result:
    print(row)

# INNER JOIN
# Connect users with their respective orders
cursor.execute("""
SELECT
    users.name,
    orders.product,
    orders.amount
FROM users
INNER JOIN orders
    ON users.id = orders.user_id
""")

result = cursor.fetchall()

print("\nINNER JOIN - Users and Their Orders:")

for row in result:
    print(row)

# Close the database connection
connection.close()

print("\nDatabase connection closed.")