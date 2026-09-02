import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models import Expense


def test_create_normalizes_category_case():
    e = Expense.create(category="food", amount=100)
    assert e.category == "Food"


def test_create_unknown_category_falls_back_to_other():
    e = Expense.create(category="Bogus", amount=50)
    assert e.category == "Other"


def test_create_empty_category_defaults_to_other():
    e = Expense.create(category="", amount=20)
    assert e.category == "Other"


def test_zero_amount_raises():
    with pytest.raises(ValueError):
        Expense.create(category="Food", amount=0)


def test_negative_amount_raises():
    with pytest.raises(ValueError):
        Expense.create(category="Food", amount=-5)


def test_round_trip_row_serialization():
    e = Expense.create(category="Travel", amount=250.5, note="Cab")
    row = e.to_row()
    rebuilt = Expense.from_row(dict(zip(["Date", "Category", "Amount", "Note"], row)))
    assert rebuilt.amount == 250.5
    assert rebuilt.category == "Travel"
    assert rebuilt.note == "Cab"
