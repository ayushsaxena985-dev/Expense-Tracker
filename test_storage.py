import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models import Expense
from storage import ExpenseRepository


def make_temp_repo():
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    os.remove(path)  # let the repo create it fresh
    return ExpenseRepository(filename=path), path


def test_initializes_empty_file_with_headers():
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


def test_clear_all_removes_entries_but_keeps_headers():
    repo, path = make_temp_repo()
    try:
        repo.add(Expense.create(category="Food", amount=10))
        repo.clear_all()
        assert repo.get_all() == []
    finally:
        os.remove(path)


def test_corrupt_row_is_skipped_not_fatal():
    repo, path = make_temp_repo()
    try:
        repo.add(Expense.create(category="Food", amount=10))
        # Manually append a malformed row (non-numeric amount)
        with open(path, "a") as f:
            f.write("2026-01-01,Food,not-a-number,broken\n")
        expenses = repo.get_all()
        assert len(expenses) == 1  # only the valid one survives
    finally:
        os.remove(path)
