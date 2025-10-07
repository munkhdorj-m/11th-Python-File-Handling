import os
from assignment import grade_report, calculate_balance


def test1(tmp_path):
    input_file = tmp_path / "grades.txt"
    output_file = tmp_path / "report.txt"

    input_file.write_text("Alice,89\nBob,72\nCharlie,95\nDiana,62\n")

    grade_report(input_file, output_file)

    result = output_file.read_text().strip()
    assert "Average: 79.5" in result
    assert "Highest: Charlie (95)" in result
    assert "Lowest: Diana (62)" in result


def test2(tmp_path):
    input_file = tmp_path / "transactions.txt"
    output_file = tmp_path / "summary.txt"

    input_file.write_text("+200\n-50\n+100\n-30\n")

    calculate_balance(input_file, output_file)

    result = output_file.read_text().strip()
    assert result == "Final Balance: 220"
