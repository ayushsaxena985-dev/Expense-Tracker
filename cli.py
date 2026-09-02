"""
Command-line interface. Only responsible for talking to the user —
all logic is delegated to services.py and storage.py.
"""

from models import Expense
from services import category_breakdown_with_percentage, total_spent
from storage import ExpenseRepository


def prompt_add_expense(repo: ExpenseRepository) -> None:
    print("\n--- Add New Expense ---")

    while True:
        raw_amount = input("Enter amount (Rs): ").strip()
        try:
            amount = float(raw_amount)
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    category = input("Enter category (Food/Travel/Shopping/Bills/Other): ").strip()
    note = input("Add a short note (optional): ").strip()

    expense = Expense.create(category=category, amount=amount, note=note)
    repo.add(expense)
    print(f"Expense of Rs {expense.amount:.2f} added under '{expense.category}'.\n")


def print_all_expenses(repo: ExpenseRepository) -> None:
    print("\n--- All Expenses ---")
    expenses = repo.get_all()

    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print(f"{'Date':<12}{'Category':<12}{'Amount':<10}{'Note'}")
    print("-" * 50)
    for e in expenses:
        print(f"{e.date:<12}{e.category:<12}{e.amount:<10.2f}{e.note}")
    print()


def print_summary(repo: ExpenseRepository) -> None:
    print("\n--- Expense Summary ---")
    expenses = repo.get_all()

    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print(f"Total Spent: Rs {total_spent(expenses):.2f}\n")
    print("Category-wise breakdown:")
    for category, amount, pct in category_breakdown_with_percentage(expenses):
        print(f"  {category:<12} Rs {amount:.2f}  ({pct:.1f}%)")
    print()


def prompt_delete_all(repo: ExpenseRepository) -> None:
    confirm = input("Are you sure you want to delete ALL expenses? (yes/no): ").strip().lower()
    if confirm == "yes":
        repo.clear_all()
        print("All expenses deleted.\n")
    else:
        print("Cancelled.\n")


def print_menu() -> None:
    print("=" * 40)
    print("        PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary (Total + Category-wise)")
    print("4. Delete All Expenses")
    print("5. Exit")


def run(repo: ExpenseRepository = None) -> None:
    """Runs the interactive menu loop. Accepts any repository that
    implements add/get_all/clear_all — CSV or SQLite — defaulting to CSV."""
    if repo is None:
        repo = ExpenseRepository()

    actions = {
        "1": prompt_add_expense,
        "2": print_all_expenses,
        "3": print_summary,
        "4": prompt_delete_all,
    }

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Thank you for using Expense Tracker. Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action(repo)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
