# purpose: write the purpose for the utility.

# import dependencies
# from pathlib import Path

# import config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util().get_config


# write utility class
class Util:
    def __init__(self, command_args=None):
        self.docstring = """Describe your utility here."""
        self.util_type = "independent"
        self.command_args = command_args

    @staticmethod
    def example_method(data_some: str, some_data: str, *extras):
        pass  # write your method here
