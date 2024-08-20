# purpose: describe your command's purpose...
# command: describe the command

# import dependencies
# import sys


# import templates and config
from utils.template_manager import Util as template_manager_util
from utils.config_manager import Util as config_manager_util

get_template = template_manager_util.get_template
get_config = config_manager_util.get_config


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "command_name_goes_here"
        self.docstring = """Describe your command here..."""
        # completely optional:
        # self.extended_docstring = """"""
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
