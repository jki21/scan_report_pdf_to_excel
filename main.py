import os.path

from ExcelExporter import export_issues
from PdfUtil import file_to_lines, lines_to_blocks
from FortifyParser import parse_issue

src_file = "test/a.pdf"


def scan_report_pdf_to_excel():
    all_lines = file_to_lines(src_file)
    all_issues = parse_issue(all_lines)
    target_path, file_name = os.path.split(src_file)
    file_name = file_name.replace(".pdf", "")
    export_issues(all_issues, target_path, file_name)


if __name__ == '__main__':
    scan_report_pdf_to_excel()
