"""Assessment 2: Simple Daily Expense Tracker."""

HIGH_EXPENSE_LIMIT = 10000

expenses = [
    {"name": "Transport", "amount": 3000},
    {"name": "Food", "amount": 4500},
    {"name": "Internet", "amount": 12000},
    {"name": "Books", "amount": 7000},
    {"name": "Data", "amount": 15000},
]


def calculate_total(expense_list):
    """Calculate and return the total amount spent."""
    total = 0
    for expense in expense_list:
        total += expense["amount"]
    return total


def main():
    high_count = 0

    print("Daily Expense Report")
    print("-------------------")

    for expense in expenses:
        if expense["amount"] > HIGH_EXPENSE_LIMIT:
            label = "High Expense"
            high_count += 1
        else:
            label = "Normal Expense"
        print(f"{expense['name']}: {expense['amount']} - {label}")

    print(f"Total Amount Spent: {calculate_total(expenses)}")
    print(f"High Expenses: {high_count}")


if __name__ == "__main__":
    main()
