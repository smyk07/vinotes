# purpose: Opens the plugins.json file in selected editor according to config
# command: vn plug

# import dependencies
import subprocess


# import templates and config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "plug"
        self.docstring = """Opens the plugins.json file, for adding plugins, editing plugin config, and related activities inside the selected text editor inside config.json."""
        # completely optional:
        # self.extended_docstring = """"""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        subprocess.run(
            f"{get_config('vim_command')} .vinotes/plugins.json",
            shell=True,
            executable=get_config("shell_executable"),
        )


# test file if run as main.
if __name__ == "__main__":
    pass  # testing code goes here.
