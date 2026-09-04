# Command-Line Expense Tracker

A simple beginner-level command-line program to track daily expenses, built in Python.

## About

This project lets you record your daily expenses, view them, and see a summary of how much you've spent overall and in each category — all from the terminal, with no external libraries or databases involved.

## Features

- **Add Expense** — record an amount, category, and short description for each expense
- **View Expenses** — list all recorded expenses
- **Show Summary** — displays:
  - Total amount spent
  - Amount spent in each category
  - The category with the highest spending
- **Exit** — closes the program
- **Input validation** — amount must be a positive number, category and description can't be empty, invalid menu choices are handled gracefully

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python expense_tracker.py
```

## Technologies Used

- Python 3 (standard library only — no external packages required)

## Concepts Used

Variables, input/output, if/elif/else, loops, lists, dictionaries, functions, and basic calculations.

## Example

```
===================================
      COMMAND-LINE EXPENSE TRACKER
===================================

1. Add Expense
2. View Expenses
3. Show Summary
4. Exit

Enter choice: 1
Amount: 250
Category: Food
Description: Lunch
Expense added successfully!
```

## Project Structure

```
expense-tracker/
└── expense_tracker.py
```