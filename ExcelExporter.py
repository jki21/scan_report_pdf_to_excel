import os.path
from typing import List
from openpyxl import Workbook

from CodeScanIssue import CodeScanIssue

column_names = ["Description", "File", "Severity"]


def export_issues(issues: List[CodeScanIssue], target_path, file_name):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(column_names)
    for issue in issues:
        sheet.append([issue.desc, issue.file, issue.severity])

    workbook.save(os.path.join(target_path, f"{file_name}.xlsx"))
