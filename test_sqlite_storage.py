import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models import Expense
from sqlite_storage import SQLiteExpenseRepository


def make_temp_repo():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    os.remove(path)  # let the repo create it fresh
    return SQLiteExpenseRepository(filename=path), path


def test_initializes_empty_db():
    repo, path = make_temp_repo()
    try:
        assert repo.get_all() == []
    finally:
        os.remove(path)


def test_add_and_get_all():
    repo, path = make_temp_repo()
    try:
        repo.add(Expense.create(category="Food", amount=99.5, note="Lunch"))
        expenses = repo.get_all()
        assert len(expenses) == 1
        assert expenses[0].category == "Food"
        assert expenses[0].amount == 99.5
    finally:
        os.remove(path)


def test_get_all_preserves_insertion_order():
    repo, path = make_temp_repo()
    try:
        repo.add(Expense.create(category="Food", amount=10))
        repo.add(Expense.create(category="Travel", amount=20))
        repo.add(Expense.create(category="Bills", amount=30))
        categories = [e.category for e in repo.get_all()]
        assert categories == ["Food", "Travel", "Bills"]
    finally:
        os.remove(path)


def test_clear_all_removes_entries():
    repo, path = make_temp_repo()
    try:
        repo.add(Expense.create(category="Food", amount=10))
        repo.clear_all()
        assert repo.get_all() == []
    finally:
        os.remove(path)
