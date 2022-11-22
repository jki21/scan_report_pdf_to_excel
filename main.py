from PdfUtil import file_to_lines, lines_to_blocks
from FortifyParser import parse_issue

src_file = "test/a.pdf"


def scan_report_pdf_to_excel():
    all_lines = file_to_lines(src_file)
    all_issues = parse_issue(all_lines)
    print(all_issues[2].to_csv())


if __name__ == '__main__':
    scan_report_pdf_to_excel()
