# purpose: Creates or Opens today's daily note
# command: vinotes open-daily

# import dependencies
import datetime
from pathlib import Path
import subprocess

# import templates and config
from utils.template_manager import Util as template_manager_util
from utils.config_manager import Util as config_manager_util

get_template = template_manager_util.get_template
get_config = config_manager_util.get_config

# setting date variable
date = datetime.datetime.now().strftime(get_config("date_format"))

# setting daily notes directory Path variable
daily_dir = Path(get_config("daily_notes_directory"))

# create file variable
file = Path(f"./{daily_dir}/{date}.md")


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "open-daily"
        self.docstring = """creates or opens today's daily note."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        # write your command here
        if file.is_file():
            open_daily()
        else:
            try:
                temp_data = get_template("daily", date)
            except ModuleNotFoundError:
                print("Cannot create file, template not found")
                quit()
            with file.open("w") as note:
                note.write(temp_data)
            open_daily()


# write helper functions here (delete the code below obv)
def open_daily(
    vim_command=f"{get_config('vim_command')}",
    executable=f"{get_config('shell_executable')}",
    filepath=f"{daily_dir}/{date}.md",
):
    subprocess.run(
        f"{vim_command} {filepath}",
        shell=True,
        executable=f"{executable}",
    )


# test file if run as main.
if __name__ == "__main__":
    test_util = Util()
    test_util.command()
