# import dependencies
import sys
import importlib
from pathlib import Path
from rich import print

# change path
sys.path.insert(0, "./.vinotes/")


# help_check function
def help_check(util=None):
    if util:
        print(f"[bold cyan]command[/] - [bold light_green]{util.name}[/]")
        if hasattr(util, "extended_docstring"):
            print(f"[bold cyan]usage[/]: {util.extended_docstring}")
        else:
            print(f"[bold cyan]usage[/]: {util.docstring}")
    else:
        print("Welcome to vinotes help,\n")
        print("[bold light_green]--help[/] - Print this help document.")
        print(
            "[bold light_green]<command> --help[/] - extended help for any command.\n"
        )

        util_files = [f for f in Path(".vinotes/utils/").iterdir() if f.is_file()]

        for file in util_files:
            if not str(file).split("/")[-1][:-3].startswith("example"):
                util_name = str(file).split("/")[-1][:-3]
                util = importlib.import_module(f"utils.{util_name}").Util()

                if util.util_type == "command":
                    print(f"[bold light_green]{util_name}[/] - {util.docstring}")
