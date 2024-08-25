# import dependencies
import sys
import importlib
from typing import Optional
from typing import List
from typing_extensions import Annotated
import typer
from rich import print


# changing path
sys.path.insert(0, "..")


# import local functions
from vinotes.help import help_check


# main function
def main(
    command: Annotated[Optional[str], typer.Argument()] = None,
    command_args: Annotated[Optional[List[str]], typer.Argument()] = None,
    help: Annotated[Optional[bool], typer.Option()] = False,
):
    """
    Welcome to Vinotes, an external markdown note-taking utility for Neovim or any other text editor.
    """

    if command is None:
        if help:
            help_check()
        else:
            print(
                "Welcome to [light_green]vinotes[/], use [bold bright_red]--help[/] for more options"
            )
    else:
        try:
            util = (
                importlib.import_module(f"utils.{command}", "..").Util(command_args)
                if command_args is not None
                else importlib.import_module(f"utils.{command}", "..").Util()
            )
            if util.util_type == "independent":
                raise ModuleNotFoundError
        except ModuleNotFoundError:
            invalid_command_provided()
            quit()

        if help:
            help_check(util)
            quit()

        util.command()


# if invalid command provided
def invalid_command_provided():
    print(
        "Invalid vinotes command, use [bold bright_red]vinotes --help[/] for more info"
    )


# run the main function
typer.run(main)
