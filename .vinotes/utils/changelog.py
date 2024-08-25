# purpose: when run, opens CHANGELOG.md in vim.
# command: vn changelog

# import packages
import sys
from pathlib import Path
import subprocess
from rich import print

# updating path
sys.path.insert(0, "..")


# import config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util().get_config


# write class
class Util:
    def __init__(self, command_args=None):
        self.name = "changelog"
        self.docstring = """Open the vinotes changelog in your text editor."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        changelog = Path("./CHANGELOG.md")
        if changelog.is_file():
            subprocess.run(
                f"{get_config('vim_command')} \"{str(changelog)}\"",
                shell=True,
                executable=f"{get_config('shell_executable')}",
            )
        else:
            print("\nFile [bold bright_red]CHANGELOG.md[/] not found...")


# test the util if run as main
if __name__ == "__main__":
    test_util = Util()
    test_util.command()
