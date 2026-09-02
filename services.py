"""
Business logic. Pure functions that operate on Expense objects only —
no file I/O, no input()/print(). This is what unit tests target.
"""

from typing import Dict, List

from models import Expense


def total_spent(expenses: List[Expense]) -> float:
    return sum(e.amount for e in expenses)


def category_breakdown(expenses: List[Expense]) -> Dict[str, float]:
    """Returns {category: total_amount}, unsorted."""
    breakdown: Dict[str, float] = {}
    for e in expenses:
        breakdown[e.category] = breakdown.get(e.category, 0.0) + e.amount
    return breakdown


def category_breakdown_with_percentage(expenses: List[Expense]) -> List[tuple]:
    """Returns [(category, amount, percentage), ...] sorted by amount desc."""
    total = total_spent(expenses)
    breakdown = category_breakdown(expenses)
    result = []
    for category, amount in breakdown.items():
        pct = (amount / total * 100) if total > 0 else 0.0
        result.append((category, amount, pct))
    return sorted(result, key=lambda x: x[1], reverse=True)
