# import dependencies
import sys
import importlib
from pathlib import Path

# change path
sys.path.insert(0, "..")


# print help func
def print_command_help(command: str, extended_docstring: str):
    print(f"Welcome to vinotes, here is help for {command}")
    print(f"\nutility: {command}")
    print(f"usage: {extended_docstring}")


# help_check function
def help_check(util=None):
    if util:
        print(f"command - {util.name}")
        if hasattr(util, "extended_docstring"):
            print(f"usage: {util.extended_docstring}")
        else:
            print(f"usage: {util.docstring}")
    else:
        print("Welcome to vinotes help,\n")
        print("--help - Print this help document")
        print("<command> --help - extended help for any command")

        util_files = [f for f in Path(".vinotes/utils/").iterdir() if f.is_file()]

        for file in util_files:
            if not str(file).split("/")[-1][:-3].startswith("example"):
                util_name = str(file).split("/")[-1][:-3]
            else:
                continue

            util = importlib.import_module(f"utils.{util_name}").Util()

            if util.util_type == "command":
                print(f"{util_name} - {util.docstring}")
