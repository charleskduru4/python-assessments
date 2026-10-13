# Assessment 2: Simple Daily Expense Tracker

A Python program that records daily expenses, flags high spending and totals the amount spent.

## Features
- Stores expenses as a list of dictionaries (`name` and `amount`)
- Loops through each expense and prints it
- Labels each expense "High Expense" (above 10,000) or "Normal Expense"
- `calculate_total()` function returns the total spent
- Displays the total and the number of high expenses

## How to Run
Requires Python 3.6+.

```bash
cd assessment2-expense-tracker
python main.py
```

## Sample Output
```
Daily Expense Report
-------------------
Transport: 3000 - Normal Expense
Food: 4500 - Normal Expense
Internet: 12000 - High Expense
Books: 7000 - Normal Expense
Data: 15000 - High Expense
Total Amount Spent: 41500
High Expenses: 2
```
