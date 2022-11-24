import os.path
from typing import List
from openpyxl import Workbook
from openpyxl.styles import Font

from CodeScanIssue import CodeScanIssue

column_names = ["#", "Description", "File", "Severity"]


def export_issues(issues: List[CodeScanIssue], target_path, file_name):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(column_names)
    for i, _ in enumerate(column_names):
        sheet.cell(column=i+1, row=1).font = Font(bold=True)

    for i, issue in enumerate(issues):
        sheet.append([i+1, issue.desc, issue.file, issue.severity])

    workbook.save(os.path.join(target_path, f"{file_name}.xlsx"))
