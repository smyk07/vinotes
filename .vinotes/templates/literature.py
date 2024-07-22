class Templates:
    def __init__(self, filename, timestamp):
        self.filename = filename
        self.timestamp = timestamp

    def content(self):
        return (
            f""
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
