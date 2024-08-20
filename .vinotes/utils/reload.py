# purpose: Checks for principle directories and the templates associated with them as described in the config.
# command: vinotes reload

# import dependencies
from pathlib import Path


# import templates and config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "reload"
        self.docstring = """Checks for principle directories and the templates associated with them as described in the config."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        # get dirs from config
        dirs_from_config = get_config("principle_dirs")
        dirs_from_config.append("daily")
        dirs_from_config.sort()

        # get existing dirs
        existing_dirs = [
            str(f)
            for f in Path("./").iterdir()
            if f.is_dir() and str(f) != ".git" and str(f) != ".vinotes"
        ]
        existing_dirs.sort()

        # getting existing templates
        existing_templates = [
            str(f).split("/")[2].split(".py")[0]
            for f in Path("./.vinotes/templates").iterdir()
            if f.is_file() and str(f) != ".vinotes/templates/example.py"
        ]

        #   consider config as the only validator
        #   first check if templates exist according to config
        #   then check if directories exist according to config
        #   handle unknown templates and directories

        for dir in dirs_from_config:
            if dir not in existing_templates:
                create_template = input(
                    f"\nTemplate for {dir} does not exist, create a simple template? (Y/n):"
                )
                if create_template == "y" or create_template == "":
                    src_template = Path(".vinotes/templates/example.py")
                    dest_template = Path(f".vinotes/templates/{dir}.py")
                    dest_template.write_text(src_template.read_text())

            if dir not in existing_dirs:
                create_dir = input(
                    f"\nPrinciple directory {dir} does not exist, create directory? (Y/n):"
                )
                if create_dir == "y" or create_dir == "":
                    dir_path = Path(f"./{dir}")
                    try:
                        dir_path.mkdir(parents=False, exist_ok=True)
                    except FileNotFoundError:
                        print("Please do not include '/' in parent directory name.")
                        print("Update .vinotes/config.json and reload again.")
                        quit()


# test file if run as main.
if __name__ == "__main__":
    pass  # testing code goes here.
