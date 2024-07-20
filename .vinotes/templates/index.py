class Templates():
    def __init__(self, filename, timestamp, quote, daily_head):
        self.quote = quote
        self.filename = filename
        self.timestamp = timestamp
        self.daily_head = daily_head

    def content(self):
        return (f"\n"
            f"# Welcome\n"
            f"\n"
            f"> {self.quote["quote"]}\n"
            f"> - {self.quote["author"]}\n"
            f"---\n"
            f"# Recent Daily Files: \n"
            f"\n"
            f"{self.daily_head}\n"
                )
