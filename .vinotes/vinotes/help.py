# import dependencies
import sys
import importlib
from pathlib import Path

# change path
sys.path.insert(0, "..")


# print help func
def print_command_help(command: str, docstring: str):
    print(f"Welcome to vinotes, here is help for {command}")
    print(f"\nutility: {command}")
    print(f"usage: {docstring}")


def print_root_help(command: str, docstring: str):
    print(f"{command} - {docstring}")


# help_check function
def help_check(help: bool = True, docstring: str = "", command=None):
    if help:
        if command is not None:
            print_command_help(command, docstring)
            quit()
        else:
            print("Welcome to vinotes help,\n")
            print("--help - Print this help document")

            utils_path = Path(".vinotes/utils/")
            util_files = utils_path.iterdir()
            for file in util_files:
                if file.is_file():
                    if not str(file).split("/")[-1][:-3].startswith("example"):
                        util_name = str(file).split("/")[-1][:-3]
                    else:
                        continue
                    util = importlib.import_module(f"utils.{util_name}", ".").Util()
                    if util.util_type == "command":
                        print(f"{util_name} - {util.docstring}")
            quit()
