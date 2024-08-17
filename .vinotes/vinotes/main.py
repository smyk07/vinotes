# import dependencies
import sys
import importlib
from typing import Optional
from typing import List
from typing_extensions import Annotated
import typer


# changing path
sys.path.insert(0, "..")


# import local functions
from vinotes.help import help_check


# if invalid command provided
def invalid_command_provided():
    print("Invalid vinotes command, use vinotes --help for more info")


# main function
def main(
    command: Annotated[Optional[str], typer.Argument()] = None,
    command_args: Annotated[Optional[List[str]], typer.Argument()] = None,
    help: Annotated[Optional[bool], typer.Option()] = False,
):
    """
    Welcome to Vinotes, an external markdown note-taking utility for Neovim or any other text editor.
    """

    if command is None and help:
        help_check()
    elif command is None and not help:
        print("Welcome to vinotes, use --help for more options")
    else:
        try:
            util = (
                importlib.import_module(f"utils.{command}", "..").Util(command_args)
                if command_args is not None
                else importlib.import_module(f"utils.{command}", "..").Util()
            )
            help_check(help=help, command=command, docstring=util.docstring)
            if util.util_type == "independent":
                raise ModuleNotFoundError
            else:
                util.command()
        except ModuleNotFoundError:
            invalid_command_provided()


# run the main function
typer.run(main)
