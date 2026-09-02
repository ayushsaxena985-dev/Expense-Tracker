import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models import Expense
from services import category_breakdown, category_breakdown_with_percentage, total_spent


def make_expenses():
    return [
        Expense(date="2026-01-01", category="Food", amount=100.0),
        Expense(date="2026-01-02", category="Food", amount=50.0),
        Expense(date="2026-01-03", category="Travel", amount=150.0),
    ]


def test_total_spent():
    assert total_spent(make_expenses()) == 300.0


def test_total_spent_empty_list():
    assert total_spent([]) == 0.0


def test_category_breakdown_sums_correctly():
    breakdown = category_breakdown(make_expenses())
    assert breakdown["Food"] == 150.0
    assert breakdown["Travel"] == 150.0


def test_category_breakdown_with_percentage_sorted_desc():
    result = category_breakdown_with_percentage(make_expenses())
    # Both categories tie at 150.0, so just check totals and percentages
    amounts = {cat: amt for cat, amt, _ in result}
    percentages = {cat: pct for cat, _, pct in result}
    assert amounts["Food"] == 150.0
    assert amounts["Travel"] == 150.0
    assert round(percentages["Food"], 1) == 50.0
    assert round(percentages["Travel"], 1) == 50.0


def test_category_breakdown_with_percentage_empty():
    assert category_breakdown_with_percentage([]) == []
