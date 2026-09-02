# Personal Expense Tracker

A command-line expense tracker built with a layered architecture: data model,
persistence, business logic, and UI are cleanly separated, making the core
logic independently unit-testable.

## Architecture

```
main.py             Entry point (picks storage backend)
cli.py               User interaction only (input/print)
services.py           Pure business logic (totals, category breakdown)
storage.py            CSV persistence (ExpenseRepository)
sqlite_storage.py      SQLite persistence (SQLiteExpenseRepository)
models.py              Expense data model with validation
tests/                 Unit tests for models, services, and both storage backends
```

Both repositories implement the same interface (`add`, `get_all`, `clear_all`),
so `services.py` and `cli.py` work unchanged regardless of which backend is used.

## Features
- Add expenses with category and amount validation
- View all expenses in a formatted table
- Category-wise spending summary with percentages
- Delete all expenses (with confirmation)
- Corrupt or malformed data rows are skipped instead of crashing the app
- Two storage backends: CSV (default) or SQLite, chosen with a flag

## Running

```bash
python main.py          # CSV storage (expenses.csv)
python main.py --db     # SQLite storage (expenses.db)
```

## Testing

```bash
pip install pytest
pytest tests/ -v
```

## Possible extensions
- Add date-range filtering and monthly reports
- Export summaries to PDF/Excel
