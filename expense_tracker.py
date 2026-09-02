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
        print()
        print("----- Expenses -----")
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            count = 1
            for item in expenses:
                print(str(count) + ". " + item["category"] + "  ₹" + item["amount"] + "  " + item["description"])
                count = count + 1

    elif choice == "3":
        print()
        print("----- Expense Summary -----")
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = 0
            category_totals = {}

            for item in expenses:
                amount = float(item["amount"])
                category = item["category"]

                total += amount

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

            for category in category_totals:
                print(category + ": ₹" + str(category_totals[category]))

            print()
            print("Total: ₹" + str(total))

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")