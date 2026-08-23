# 💰 Personal Expense Tracker (Python CLI Project)

A simple command-line application built in Python to track daily personal expenses.
Users can add expenses, view all records, and see a category-wise spending summary —
all data is saved permanently in a CSV file.

## Features
- ✅ Add new expenses with amount, category, date (auto-filled), and note
- ✅ View all recorded expenses in a clean table
- ✅ Get a summary: total spend + category-wise breakdown with percentages
- ✅ Delete all data (with confirmation)
- ✅ Input validation (handles invalid/negative amounts gracefully)
- ✅ Data persists between runs using a CSV file (no external database needed)

## Tech Stack / Concepts Used
- Python 3
- `csv` module for file-based data storage
- `datetime` module for auto date-stamping
- Functions, loops, conditionals, dictionaries
- Basic error/exception handling
- Menu-driven CLI design

## How to Run
```bash
python expense_tracker.py
```

Follow the on-screen menu to add expenses, view them, or see your spending summary.

## Sample Output
```
========================================
        PERSONAL EXPENSE TRACKER
========================================
1. Add Expense
2. View All Expenses
3. View Summary (Total + Category-wise)
4. Delete All Expenses
5. Exit
Enter your choice (1-5): 3

--- Expense Summary ---
Total Spent: Rs 1700.00

Category-wise breakdown:
  Travel       Rs 1200.00  (70.6%)
  Food         Rs 500.00  (29.4%)
```

## Future Improvements
- Add a GUI using Tkinter
- Switch from CSV to SQLite database
- Add monthly/weekly filtering
- Export summary as PDF report

## Author
<Your Name>
