class Templates():
    def __init__(self, filename, timestamp, quote):
        self.quote = quote
        self.filename = filename
        self.timestamp = timestamp

    def content(self):
        return (f"\n"
            f"# Welcome\n"
            f"\n"
            f"> {self.quote["quote"]}\n"
            f"> - {self.quote["author"]}\n"
            f"---\n"
                )
