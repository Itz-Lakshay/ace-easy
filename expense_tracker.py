# Command-Line Expense Tracker
# A simple beginner project to track daily expenses

print("========================================")
print("      COMMAND-LINE EXPENSE TRACKER      ")
print("========================================")

print("1. Add Expense")
print("2. View Expenses")
print("3. Show Summary")
print("4. Exit")

# List to store all expenses
expenses = []

# For now, just test adding one expense
amount = input("Amount: ")
category = input("Category: ")
description = input("Description: ")

expense = {
    "amount": amount,
    "category": category,
    "description": description
}

expenses.append(expense)

print("Expense added successfully!")
print(expenses)