from PyPDF2 import PdfReader


def grib_lines_until(lines, end_of_block):
    if not lines:
        return
    for line in lines:
        if line.startswith(end_of_block):
            return
        else:
            yield line


def skip_to_text(lines, text):
    line_before = list(grib_lines_until(lines, text))
    if line_before:
        return lines[len(line_before):]
    return lines


def lines_to_blocks(lines, block_seperator):
    blocks = []
    while lines:
        lines = skip_to_text(lines, block_seperator)
        temp_block = list(grib_lines_until(lines[1:], block_seperator))
        if temp_block:
            blocks += [temp_block]
            lines = lines[len(temp_block):]
        else:
            break
    return blocks


def file_to_lines(file_name):
    reader = PdfReader(file_name)
    return [lines for page in reader.pages for lines in page.extract_text().splitlines()]
