import os.path

from ExcelExporter import export_issues
from PdfUtil import file_to_lines, lines_to_blocks
from FortifyParser import parse_issue

# src_file = "test/a.pdf"


def get_file_path():
    user_input = input("Enter the path of report pdf file: ")

    assert os.path.exists(user_input), "I did not find the file at, " + str(user_input)
    return user_input


def scan_report_pdf_to_excel():
    src_file = get_file_path()
    all_lines = file_to_lines(src_file)
    all_issues = parse_issue(all_lines)
    target_path, file_name = os.path.split(src_file)
    file_name = file_name.replace(".pdf", "")
    export_issues(all_issues, target_path, file_name)


if __name__ == '__main__':
    scan_report_pdf_to_excel()
