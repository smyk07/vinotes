#!/usr/bin/python3

# purpose: when run, opens the config.json file in nano.
# command: vinotes conf

# import dependencies
import subprocess


class Util:
    def __init__(self) -> None:
        self.docstring = """Edit vinotes configuration inside nano."""
        self.util_type = "command"

    def command(self):
        subprocess.run("nano .vinotes/config.json", shell=True, executable="/bin/bash")
