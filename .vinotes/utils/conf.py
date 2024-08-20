#!/usr/bin/python3

# purpose: when run, opens the config.json file in nano.
# command: vinotes conf

# import dependencies
import subprocess


class Util:
    def __init__(self, command_args=None):
        self.name = "conf"
        self.docstring = """Edit vinotes configuration inside nano."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        subprocess.run("nano .vinotes/config.json", shell=True, executable="/bin/bash")


# test the util if run as main
if __name__ == "__main__":
    test_util = Util()
    test_util.command()
