import os
import tempfile
from project import add_expense, get_summary, export_report

def test_add_expense_and_summary(tmp_path):
    csv_file = tmp_path / "test_expenses.csv"
    # ensure file not exists initially
    assert not csv_file.exists()

    # add expenses
    assert add_expense(10.0, "Food", "Breakfast", str(csv_file))
    assert add_expense(25.5, "Transport", "Taxi", str(csv_file))
    assert add_expense(5.0, "Food", "Snack", str(csv_file))

    # now summary
    summary = get_summary(str(csv_file))
    assert summary["count"] == 3
    # totals: 10 + 25.5 + 5 = 40.5
    assert abs(summary["total"] - 40.5) < 1e-6
    # categories
    assert "Food" in summary["by_category"]
    assert "Transport" in summary["by_category"]
    assert abs(summary["by_category"]["Food"] - 15.0) < 1e-6
    assert abs(summary["by_category"]["Transport"] - 25.5) < 1e-6

def test_export_report_creates_file(tmp_path):
    csv_file = tmp_path / "test_expenses2.csv"
    out_report = tmp_path / "report.txt"
    # add one expense
    assert add_expense(100.0, "Rent", "Monthly", str(csv_file))
    # export
    export_report(str(csv_file), str(out_report))
    assert out_report.exists()
    content = out_report.read_text(encoding="utf-8")
    assert "Total entries" in content or "Total entries:" in content
    assert "Total spent" in content
    assert "Rent" in content

def test_add_invalid_amount_fails(tmp_path):
    csv_file = tmp_path / "test_invalid.csv"
    # passing negative amount should return False
    assert not add_expense(-5.0, "Misc", "Negative", str(csv_file))
    # file should still not exist or be empty
    if os.path.exists(str(csv_file)):
        summary = get_summary(str(csv_file))
        assert summary["count"] == 0
