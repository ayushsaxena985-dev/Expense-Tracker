"""
SQLite persistence layer. Drop-in replacement for ExpenseRepository
(storage.py) — same public interface (add, get_all, clear_all), so
nothing in services.py or cli.py needs to change to use this instead.
"""

import sqlite3
from typing import List

from models import Expense


class SQLiteExpenseRepository:
    """Handles reading and writing expenses to a SQLite database."""

    def __init__(self, filename: str = "expenses.db"):
        self.filename = filename
        self._initialize_db()

    def _initialize_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    note TEXT DEFAULT ''
                )
                """
            )

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.filename)

    def add(self, expense: Expense) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
                (expense.date, expense.category, expense.amount, expense.note),
            )

    def get_all(self) -> List[Expense]:
        """Return all valid expenses. Corrupt rows are skipped, not fatal."""
        expenses = []
        with self._connect() as conn:
            cursor = conn.execute("SELECT date, category, amount, note FROM expenses ORDER BY id")
            for date, category, amount, note in cursor.fetchall():
                try:
                    expenses.append(
                        Expense(date=date, category=category, amount=float(amount), note=note or "")
                    )
                except (ValueError, TypeError):
                    # Skip malformed rows instead of crashing the whole app.
                    continue
        return expenses

    def clear_all(self) -> None:
        with self._connect() as conn:
            conn.execute("DELETE FROM expenses")
