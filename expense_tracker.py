"""
Personal Expense Tracker
-------------------------
A simple command-line application to add, view, and analyze personal expenses.
Data is stored in a CSV file so it persists between runs.

Author: <Your Name>
"""

import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"
FIELDS = ["Date", "Category", "Amount", "Note"]


def initialize_file():
    """Create the CSV file with headers if it doesn't already exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)


def add_expense():
    """Ask the user for expense details and save them to the CSV file."""
    print("\n--- Add New Expense ---")

    # Validate amount input
    while True:
        amount = input("Enter amount (Rs): ").strip()
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    category = input("Enter category (Food/Travel/Shopping/Bills/Other): ").strip().title()
    if category == "":
        category = "Other"

    note = input("Add a short note (optional): ").strip()

    date_today = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_today, category, amount, note])

    print(f"Expense of Rs {amount} added under '{category}'.\n")


def view_expenses():
    """Display all recorded expenses in a readable table format."""
    print("\n--- All Expenses ---")

    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.\n")
        return

    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.\n")
        return

    print(f"{'Date':<12}{'Category':<12}{'Amount':<10}{'Note'}")
    print("-" * 50)
    for row in rows:
        print(f"{row['Date']:<12}{row['Category']:<12}{row['Amount']:<10}{row['Note']}")
    print()


def show_summary():
    """Show total expense and a category-wise breakdown."""
    print("\n--- Expense Summary ---")

    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.\n")
        return

    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.\n")
        return

    total = 0.0
    category_totals = {}

    for row in rows:
        amount = float(row["Amount"])
        category = row["Category"]
        total += amount
        category_totals[category] = category_totals.get(category, 0) + amount

    print(f"Total Spent: Rs {total:.2f}\n")
    print("Category-wise breakdown:")
    for category, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        percentage = (amt / total) * 100
        print(f"  {category:<12} Rs {amt:.2f}  ({percentage:.1f}%)")
    print()


def delete_all_expenses():
    """Reset the expense file after user confirmation."""
    confirm = input("Are you sure you want to delete ALL expenses? (yes/no): ").strip().lower()
    if confirm == "yes":
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)
        print("All expenses deleted.\n")
    else:
        print("Cancelled.\n")


def print_menu():
    print("=" * 40)
    print("        PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary (Total + Category-wise)")
    print("4. Delete All Expenses")
    print("5. Exit")


def main():
    initialize_file()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            delete_all_expenses()
        elif choice == "5":
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
