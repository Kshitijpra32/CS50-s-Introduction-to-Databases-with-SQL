#!/usr/bin/env python3
"""
Smart Expense Tracker
project.py - main entrypoint and functions required by CS50P final project.
"""

from datetime import datetime
import csv
import os
from typing import Dict, Tuple
import pandas as pd
import matplotlib.pyplot as plt


DEFAULT_CSV = "expenses.csv"


def main():
    """
    Simple CLI loop: add, summary, visualize, export, or quit.
    """
    print("Smart Expense Tracker")
    csv_file = DEFAULT_CSV

    while True:
        print("\nChoose an option:")
        print("1) Add expense")
        print("2) View summary")
        print("3) Visualize expenses (generates 'expenses_plot.png')")
        print("4) Export report (report.txt)")
        print("5) Quit")
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            amount = input("Amount (e.g. 23.50): ").strip()
            category = input("Category (e.g. Food, Rent): ").strip()
            desc = input("Description (optional): ").strip()
            try:
                amount_f = float(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            success = add_expense(amount_f, category, desc, csv_file)
            if success:
                print("Expense recorded.")
            else:
                print("Failed to record expense.")
        elif choice == "2":
            summary = get_summary(csv_file)
            print_summary(summary)
        elif choice == "3":
            out = "expenses_plot.png"
            visualize_expenses(csv_file, out)
            print(f"Saved visualization to {out}")
        elif choice == "4":
            out = "report.txt"
            export_report(csv_file, out)
            print(f"Saved report to {out}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


# --------------------------
# Core functions (for tests)
# --------------------------

def _ensure_csv_exists(filename: str) -> None:
    """Create CSV with header if it doesn't exist."""
    if not os.path.exists(filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "amount", "category", "description"])


def add_expense(amount: float, category: str, description: str = "", filename: str = DEFAULT_CSV) -> bool:
    """
    Append an expense row to CSV.
    Returns True on success, False on failure.
    """
    try:
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        _ensure_csv_exists(filename)
        now = datetime.utcnow().isoformat()
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([now, f"{amount:.2f}", category.strip() or "Uncategorized", description.strip()])
        return True
    except Exception:
        return False


def get_summary(filename: str = DEFAULT_CSV) -> Dict[str, object]:
    """
    Return summary dict:
    {
      "total": float,
      "by_category": {category: float, ...},
      "count": int,
    }
    If no file or no rows, returns zeros/empty dict.
    """
    if not os.path.exists(filename):
        return {"total": 0.0, "by_category": {}, "count": 0}

    try:
        df = pd.read_csv(filename)
        if df.empty:
            return {"total": 0.0, "by_category": {}, "count": 0}
        # ensure amount numeric
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
        total = float(df["amount"].sum())
        by_cat_series = df.groupby("category")["amount"].sum().sort_values(ascending=False)
        by_category = {str(k): float(v) for k, v in by_cat_series.items()}
        count = int(len(df))
        return {"total": total, "by_category": by_category, "count": count}
    except Exception:
        return {"total": 0.0, "by_category": {}, "count": 0}


def visualize_expenses(filename: str = DEFAULT_CSV, out_png: str = "expenses_plot.png") -> None:
    """
    Generate a pie chart of category-wise spending and save to out_png.
    If no data, create a small placeholder image.
    """
    summary = get_summary(filename)
    by_category = summary["by_category"]
    if not by_category:
        # Create an empty placeholder figure
        fig = plt.figure(figsize=(4, 3))
        plt.text(0.5, 0.5, "No data", ha="center", va="center")
        plt.axis("off")
        fig.savefig(out_png, bbox_inches="tight")
        plt.close(fig)
        return

    labels = list(by_category.keys())
    sizes = list(by_category.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    plt.title("Spending by Category")
    fig.savefig(out_png, bbox_inches="tight")
    plt.close(fig)


def export_report(filename: str = DEFAULT_CSV, out_txt: str = "report.txt") -> None:
    """
    Export a plain-text report containing totals and category breakdown.
    """
    summary = get_summary(filename)
    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("Smart Expense Tracker Report\n")
        f.write("============================\n\n")
        f.write(f"Total entries: {summary['count']}\n")
        f.write(f"Total spent: {summary['total']:.2f}\n\n")
        f.write("Spent by category:\n")
        if not summary["by_category"]:
            f.write("  (no data)\n")
        else:
            for cat, amt in summary["by_category"].items():
                f.write(f"  {cat}: {amt:.2f}\n")


# --------------------------
# Helper for CLI printing
# --------------------------
def print_summary(summary: Dict[str, object]) -> None:
    print("\nExpense Summary")
    print("----------------")
    print(f"Entries: {summary.get('count', 0)}")
    print(f"Total spent: {summary.get('total', 0.0):.2f}")
    print("By category:")
    by_cat = summary.get("by_category", {})
    if not by_cat:
        print("  (no data)")
    else:
        for cat, amt in by_cat.items():
            print(f"  {cat}: {amt:.2f}")


if __name__ == "__main__":
    main()
