"""
Personal Expense Tracker
-------------------------
A command-line application to add, view, and analyze personal expenses.
Data is stored in a CSV file so it persists between runs.

Architecture:
    models.py   - Expense data model (validation, serialization)
    storage.py  - CSV persistence (ExpenseRepository)
    services.py - Business logic (totals, category breakdown)
    cli.py      - User interaction (input/output only)

Author: <Ayush>
"""

from cli import run

if __name__ == "__main__":
    run()
