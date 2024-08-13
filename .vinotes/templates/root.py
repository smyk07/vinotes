class Templates:
    def __init__(self, filename: str, timestamp: str):
        self.filename = filename
        self.timestamp = timestamp

    def content(self):
        return (
            f"---\n"
            f"title: {self.filename}\n"
            f"creation: {self.timestamp}\n"
            f"tags: \n"
            f"---\n"
            f"\n"
            f"# {self.filename}\n"
            f"\n"
            f"\n"
            f"\n"
            f"---\n"
            f"# Links & References\n"
            f"\n"
            f"- \n"
            f"\n"
            f"---\n"
        )
