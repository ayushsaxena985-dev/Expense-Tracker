"""
Data model for a single expense entry.
"""

from dataclasses import dataclass
from datetime import datetime


VALID_CATEGORIES = {"Food", "Travel", "Shopping", "Bills", "Other"}


@dataclass(frozen=True)
class Expense:
    """Represents a single expense record."""

    date: str
    category: str
    amount: float
    note: str = ""

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if self.category not in VALID_CATEGORIES:
            object.__setattr__(self, "category", "Other")

    @staticmethod
    def create(category: str, amount: float, note: str = "") -> "Expense":
        """Factory that stamps today's date and normalizes the category."""
        category = (category or "").strip().title() or "Other"
        return Expense(
            date=datetime.now().strftime("%Y-%m-%d"),
            category=category,
            amount=float(amount),
            note=(note or "").strip(),
        )

    def to_row(self) -> list:
        """Serialize to a CSV row."""
        return [self.date, self.category, f"{self.amount:.2f}", self.note]

    @staticmethod
    def from_row(row: dict) -> "Expense":
        """Deserialize from a CSV DictReader row. Raises ValueError on bad data."""
        return Expense(
            date=row["Date"],
            category=row["Category"],
            amount=float(row["Amount"]),
            note=row.get("Note", ""),
        )
