# purpose: provides template content to note-creating scripts.
# command: none

# import modules
import sys
import datetime
import importlib

# import config
from config_manager import Util as config_manager_util

get_config = config_manager_util().get_config

# updating path
sys.path.insert(0, "..")

# get timestamp
ct = datetime.datetime.now()
timestamp = ct.strftime(get_config("timestamp_format"))


class Util:
    def __init__(self) -> None:
        self.docstring = """Provides template data."""
        self.util_type = "independent"

    @staticmethod
    def get_template(func: str, filename: str, *extras):
        try:
            template_module = importlib.import_module(f"templates.{func}", ".")
            template = template_module.Templates(filename, timestamp, *extras)
            return template.content()
        except ModuleNotFoundError:
            raise ModuleNotFoundError
