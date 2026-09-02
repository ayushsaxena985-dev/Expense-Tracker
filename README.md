# Personal Expense Tracker

A command-line expense tracker built with a layered architecture: data model,
persistence, business logic, and UI are cleanly separated, making the core
logic independently unit-testable.

## Architecture

```
main.py       Entry point
cli.py        User interaction only (input/print)
services.py   Pure business logic (totals, category breakdown)
storage.py    CSV persistence (ExpenseRepository)
models.py     Expense data model with validation
tests/        Unit tests for models, services, and storage
```

## Features
- Add expenses with category and amount validation
- View all expenses in a formatted table
- Category-wise spending summary with percentages
- Delete all expenses (with confirmation)
- Corrupt or malformed CSV rows are skipped instead of crashing the app

## Running

```bash
python main.py
```

## Testing

```bash
pip install pytest
pytest tests/ -v
```

## Possible extensions
- Swap `ExpenseRepository` for a SQLite-backed implementation without
  touching `services.py` or `cli.py`
- Add date-range filtering and monthly reports
- Export summaries to PDF/Excel
