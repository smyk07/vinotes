# purpose: provides template content to note-creating scripts.

# import modules
import sys
import datetime
import importlib

# updating path
sys.path.insert(0, "..")

# import config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util().get_config


# get timestamp
ct = datetime.datetime.now()
timestamp = ct.strftime(get_config("timestamp_format"))


class Util:
    def __init__(self, command_args=None):
        self.docstring = """Provides template data (this is an independent utility, and thus not accessible through a command)."""
        self.util_type = "independent"
        self.command_args = command_args

    @staticmethod
    def get_template(func: str, filename: str, *extras):
        try:
            template_module = importlib.import_module(f"templates.{func}", ".")
            template = template_module.Templates(filename, timestamp, *extras)
            return template.content()
        except ModuleNotFoundError:
            raise ModuleNotFoundError
