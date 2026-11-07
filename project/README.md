# Smart Expense Tracker

#### Video Demo: <URL TO YOUR VIDEO>

#### Description:
Smart Expense Tracker is a small Python project that helps users record, summarize, visualize, and export their expenses. It is designed as a command-line tool to keep dependencies minimal and to focus on the core functionality expected of a CS50P final project.

This project satisfies CS50P final project requirements:
- Implemented in Python.
- Contains a `main()` in `project.py` and at least three additional top-level functions (`add_expense`, `get_summary`, `visualize_expenses`, `export_report`).
- Tests for three functions are provided in `test_project.py` (executable with `pytest`).
- Uses CSV for persistent storage and produces a PNG visualization and a TXT report.

#### Files:
- `project.py` — main program file. Contains:
  - `main()` — CLI entrypoint.
  - `add_expense(amount, category, description, filename)` — appends an expense to a CSV.
  - `get_summary(filename)` — computes total spending and category breakdown.
  - `visualize_expenses(filename, out_png)` — writes a pie chart to a PNG file.
  - `export_report(filename, out_txt)` — creates a human-readable `report.txt`.
  - Helper functions for CSV setup and printing.

- `test_project.py` — pytest tests for:
  - adding expenses and validating summary totals,
  - exporting a report,
  - ensuring invalid negative amounts are rejected.

- `requirements.txt` — lists `pandas` and `matplotlib`.

#### How to run:
1. (Optional) create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
