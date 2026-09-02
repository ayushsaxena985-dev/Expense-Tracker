"""
Personal Expense Tracker
-------------------------
A command-line application to add, view, and analyze personal expenses.
Supports two storage backends: CSV (default) or SQLite.

Architecture:
    models.py          - Expense data model (validation, serialization)
    storage.py          - CSV persistence (ExpenseRepository)
    sqlite_storage.py   - SQLite persistence (SQLiteExpenseRepository)
    services.py          - Business logic (totals, category breakdown)
    cli.py               - User interaction (input/output only)

Usage:
    python main.py            # uses expenses.csv (default)
    python main.py --db       # uses expenses.db (SQLite)

Author: <Ayush>
"""

import sys

from cli import run
from storage import ExpenseRepository
from sqlite_storage import SQLiteExpenseRepository

if __name__ == "__main__":
    if "--db" in sys.argv:
        print("Using SQLite storage (expenses.db)\n")
        repo = SQLiteExpenseRepository()
    else:
        print("Using CSV storage (expenses.csv)\n")
        repo = ExpenseRepository()

    run(repo)
