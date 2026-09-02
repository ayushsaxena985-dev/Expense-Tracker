"""
Persistence layer. All file I/O lives here so the rest of the app never
touches the filesystem directly and can be tested without real files.
"""

import csv
import os
from typing import List

from models import Expense

FIELDS = ["Date", "Category", "Amount", "Note"]


class ExpenseRepository:
    """Handles reading and writing expenses to a CSV file."""

    def __init__(self, filename: str = "expenses.csv"):
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self) -> None:
        if not os.path.exists(self.filename):
            with open(self.filename, mode="w", newline="") as f:
                csv.writer(f).writerow(FIELDS)

    def add(self, expense: Expense) -> None:
        with open(self.filename, mode="a", newline="") as f:
            csv.writer(f).writerow(expense.to_row())

    def get_all(self) -> List[Expense]:
        """Return all valid expenses. Corrupt rows are skipped, not fatal."""
        if not os.path.exists(self.filename):
            return []

        expenses = []
        with open(self.filename, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    expenses.append(Expense.from_row(row))
                except (ValueError, KeyError):
                    # Skip malformed rows instead of crashing the whole app.
                    continue
        return expenses

    def clear_all(self) -> None:
        with open(self.filename, mode="w", newline="") as f:
            csv.writer(f).writerow(FIELDS)
