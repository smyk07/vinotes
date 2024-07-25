# purpose: provides template content to note-creating scripts.
# command: none

# import modules
import sys
import datetime
import importlib

# import config
from config_manager import get_config

# inserting to path
sys.path.insert(0, "..")

# get timestamp
ct = datetime.datetime.now()
timestamp = ct.strftime(get_config("timestamp_format"))


# manage templating
def get_template(func, filename, *extras):
    try:
        template_module = importlib.import_module(f"templates.{func}", ".")
        template = template_module.Templates(filename, timestamp, *extras)
        return template.content()
    except ModuleNotFoundError:
        raise ModuleNotFoundError
