import csv

expenses = []


def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["amount", "category", "description"]
        )

        writer.writeheader()
        writer.writerows(expenses)


def load_expenses():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expense = {
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "description": row["description"]
                }

                expenses.append(expense)

    except FileNotFoundError:
        pass


def add_expense():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n========== YOUR EXPENSES ==========")

    for number, expense in enumerate(expenses, start=1):
        print("Expense #", number)
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("--------------------------------")


def total_spending():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\nTotal spending:", total)


def category_summary():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n========== CATEGORY SUMMARY ==========")

    for category in category_totals:
        print(category, ":", category_totals[category])


def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    print("\n========== YOUR EXPENSES ==========")

    for number, expense in enumerate(expenses, start=1):
        print(
            number,
            "|",
            expense["amount"],
            "|",
            expense["category"],
            "|",
            expense["description"]
        )

    while True:
        try:
            number = int(input("Enter expense number to delete: "))

            if number < 1 or number > len(expenses):
                print("Invalid expense number.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    deleted_expense = expenses.pop(number - 1)

    save_expenses()

    print("Expense deleted successfully.")
    print("Deleted:", deleted_expense["description"])


load_expenses()


while True:
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Summary")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-6.")