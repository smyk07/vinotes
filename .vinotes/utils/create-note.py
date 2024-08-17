# purpose: creates a note by taking in the directory's name and the filename to create
#          and then will create a file with the given name inside of the directory
#          specified and apply the template specific to the directory.
# command: vinotes create-note <path/to/note>

# import dependencies
import sys
import subprocess
from pathlib import Path

# updating path
sys.path.insert(0, "..")

# import templates and config
from utils.template_manager import Util as template_manager_util
from utils.config_manager import Util as config_manager_util

get_template = template_manager_util.get_template
get_config = config_manager_util.get_config


# write class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.docstring = """Create a note in either the root directory, or enter a filepath including a principle directory."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        # filepath in string format
        if self.command_args != []:
            filepathstr = ""
            for i in self.command_args:
                filepathstr = f"{filepathstr} {i}"
            filepathstr = f"./{filepathstr[1:]}.md"
            file = Path(filepathstr)
        else:
            print("Please enter a path to your note")
            print("Correct usage:")
            print("vinotes create-note <path/to/note>")
            quit()

        # extract template from filepathstr
        filepathstr_split = filepathstr.split("/")
        template = filepathstr_split[1] if len(filepathstr_split) >= 3 else "root"

        # quit if template is daily
        if template == "daily":
            print("Please use vinotes open-daily to open today's daily note")
            quit()

        # create file and write contents, optionally open, if exists, ask weather to open.
        if file.is_file():
            print(f"{filepathstr} exists.")
            open_note = input("Open note? (Y/n): ")
            if open_note == "y" or open_note == "":
                open_with_editor(get_config("vim_command"), filepathstr)
        else:
            try:
                temp_data = get_template(template, filepathstr_split[-1][:-3])
            except ModuleNotFoundError:
                print("Template not found...")
                quit()
            with file.open("w") as note:
                note.write(temp_data)
            if get_config("open_note_when_created"):
                open_with_editor(get_config("vim_command"), filepathstr)


# helper functions
def open_with_editor(vim_command: str, file_path: str):
    subprocess.run(
        f'{vim_command} "{file_path}"',
        shell=True,
        executable=f"{get_config('shell_executable')}",
    )


# test file if run as main.
if __name__ == "__main__":
    test_util = Util(sys.argv[1:])
    test_util.command()
