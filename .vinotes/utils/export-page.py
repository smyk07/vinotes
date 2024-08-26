# purpose: Exports the selected note into the chosen option (either PDF or HTML)
# command: vn export-page <filepath> <export_type> OR vn export-page (fzf)

# import dependencies
# import sys


# import templates and config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "export-page"
        self.docstring = (
            """Exports the selected note into the chosen option (either PDF or HTML)"""
        )
        # completely optional:
        self.extended_docstring = """Exports your notes to optional formats. When run, either give the filepath and export type as args, or run the command by itself and select both through a fuzzy finder."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        # write your command here
        pass  # delete this line


# write helper functions here (delete the code below obv)
# def helper_func1():
#     pass

# test file if run as main.
if __name__ == "__main__":
    pass  # testing code goes here.
