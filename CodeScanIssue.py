class CodeScanIssue:
    def __init__(self, desc="N/A", file="", severity=""):
        self.desc = desc
        self.file = file
        self.severity = severity

    def to_csv(self):
        return str.join(",", [self.desc, self.file, self.severity])
