# Command-Line Expense Tracker
# A simple beginner project to track daily expenses

print("========================================")
print("      COMMAND-LINE EXPENSE TRACKER      ")
print("========================================")

# List to store all expenses
expenses = []

while True:
    print()
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")
    print()

    choice = input("Enter choice: ")

    if choice == "1":
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

    elif choice == "2":
        print("View Expenses - coming soon")

    elif choice == "3":
        print("Show Summary - coming soon")

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")