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
        # Validate amount
        while True:
            amount_input = input("Amount: ")
            try:
                amount_value = float(amount_input)
                if amount_value <= 0:
                    print("Amount must be greater than zero. Try again.")
                else:
                    break
            except ValueError:
                print("Invalid amount. Please enter a number.")

        # Validate category
        while True:
            category = input("Category: ")
            if category.strip() == "":
                print("Category cannot be empty. Try again.")
            else:
                break

        # Validate description
        while True:
            description = input("Description: ")
            if description.strip() == "":
                print("Description cannot be empty. Try again.")
            else:
                break

        expense = {
            "amount": str(amount_value),
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

            # Find the highest spending category
            highest_category = ""
            highest_amount = 0

            for category in category_totals:
                if category_totals[category] > highest_amount:
                    highest_amount = category_totals[category]
                    highest_category = category

            print()
            print("Highest spending category: " + highest_category)
            print("Amount spent: ₹" + str(highest_amount))

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")