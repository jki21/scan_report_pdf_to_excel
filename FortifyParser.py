from PdfUtil import lines_to_blocks
from CodeScanIssue import CodeScanIssue

big_block_seperator = "Engine Breakdown"
small_block_seperator = "Sink Details"


def get_desc_and_serv(lines):
    for i, line in enumerate(lines):
        if line.startswith("Package:") and i > 0:
            words = str.split(lines[i - 1], " ")
            return {"desc": str.join(" ", words[:-1]), "serv": words[len(words) - 1] if words else ""}
    return ""


def get_file_from_sink(sink_lines):
    for line in sink_lines:
        if line.startswith("File: "):
            return line.replace("File: ", "").strip()
    return ""


def parse_issue(lines):
    big_blocks = lines_to_blocks(lines, big_block_seperator)
    all_issues = []
    for block in big_blocks:
        block_info = get_desc_and_serv(block)
        small_blocks = [lines for lines in lines_to_blocks(block, small_block_seperator)]
        issue_file_list = [get_file_from_sink(sink_block) for sink_block in small_blocks]
        all_issues += [CodeScanIssue(block_info["desc"], file, block_info["serv"]) for file in issue_file_list]
    return all_issues
