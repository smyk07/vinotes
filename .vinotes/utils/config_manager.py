# purpose: convert config.json's data to a python dictionary,
#          and return the data requested through a function get_config()
# command: none

# import dependencies
import os
import sys
import json

# update path for accessing config file
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", ".vinotes"))
)


# define class
class Util:
    def __init__(self) -> None:
        self.docstring = """Gives access of configurations to other utils."""
        self.util_type = "independent"

    @staticmethod
    def get_config(key: str):
        with open(".vinotes/config.json", "r") as data:
            config = json.load(data)
        try:
            return config[key]
        except KeyError:
            raise Exception(f"cannot find config field {key}")

    @staticmethod
    def get_dev_config(key: str):
        with open(".vinotes/dev.config.json", "r") as data:
            dev_config = json.load(data)
        try:
            return dev_config[key]
        except KeyError:
            raise Exception(f"cannot find dev config field {key}")
