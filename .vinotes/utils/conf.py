#!/usr/bin/python3

# purpose: when run, opens the config.json file in nano.
# command: vinotes conf

# import dependencies
import subprocess

# get config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config


class Util:
    def __init__(self, command_args=None):
        self.name = "conf"
        self.docstring = """Edit vinotes configuration inside nano."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        subprocess.run(
            "nano .vinotes/config.json",
            shell=True,
            executable=get_config("shell_executable"),
        )


# test the util if run as main
if __name__ == "__main__":
    test_util = Util()
    test_util.command()
