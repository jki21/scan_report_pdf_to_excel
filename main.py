from PyPDF2 import PdfReader
src_file = "test/a.pdf"
big_block_seperator = "Engine Breakdown"
small_block_seperator = "Sink Details"


def get_one_block(lines, end_of_block):
    if not lines:
        return
    for line in lines:
        if line.startswith(end_of_block):
            return
        else:
            yield line


def skip_to_text(lines, text):
    for i, line in enumerate(lines):
        if line.startswith(text):
            return lines[i:]
    return []


def lines_to_blocks(lines, block_seperator):
    blocks = []
    while lines:
        lines = skip_to_text(lines, block_seperator)
        temp_block = list(get_one_block(lines[1:], block_seperator))
        if temp_block:
            blocks += [temp_block]
            lines = lines[len(temp_block):]
        else:
            break
    return blocks


def file_to_lines(file_name):
    reader = PdfReader(file_name)
    return [lines for page in reader.pages for lines in page.extract_text().splitlines()]


def scan_pdf_to_excel():
    all_lines = file_to_lines(src_file)
    big_blocks = lines_to_blocks(all_lines, big_block_seperator)
    small_blocks = [lines for block in big_blocks for lines in lines_to_blocks(block, small_block_seperator)]
    print([line for line in small_blocks[0]])


if __name__ == '__main__':
    scan_pdf_to_excel()