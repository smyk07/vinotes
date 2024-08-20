# purpose: script for opening notes by taking in the note's path or by fuzzy finding into all of the principle directories.

# command: vinotes open-note OR vinotes open-note <path/to/note>

# import dependencies
import sys
from pathlib import Path
import subprocess


# import templates and config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "open-note"
        self.docstring = """When used by itself, opens a fuzzy finder to search through all notes and opens them, when provided a filepath, open it into text editor."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        # write your command here
        if self.command_args == []:
            # do the fzf thing to assign filepath
            dirs = "".join(f"{dir} " for dir in get_config("principle_dirs"))
            try:
                file_path = Path(
                    subprocess.check_output(
                        f"find ./ {dirs} \\( -iname '*.md' \\) -type f | fzf",
                        shell=True,
                        executable=f"{get_config('shell_executable')}",
                    ).decode("utf-8")[:-1]
                )
            except subprocess.CalledProcessError:
                quit()
        else:
            # assign filepath to organized command_args
            file_path = self.command_args[0]

        # open file
        if file_path.is_file():
            subprocess.run(
                f"{get_config('vim_command')} \"{str(file_path)}\"",
                shell=True,
                executable=f"{get_config('shell_executable')}",
            )
        else:
            print("\nPlease enter a valid file path.")


# test file if run as main.
if __name__ == "__main__":
    test_util = Util(sys.argv[1:])
    test_util.command()
