# purpose: convert config.json's data to a python dictionary,
#          and return the data requested through a function get_config()

# import dependencies
import sys
import json

# update path for accessing config file
sys.path.insert(0, "..")


# define class
class Util:
    def __init__(self, command_args=None):
        self.docstring = """Gives access of configurations to other utils (this is an independent utility, and this not accessible through a command)."""
        self.util_type = "independent"
        self.command_args = command_args

    @staticmethod
    def get_config(key: str):
        with open(".vinotes/config.json", "r") as data:
            config = json.load(data)
        try:
            return config[key]
        except KeyError:
            raise Exception(f"cannot find config field {key}")

    @staticmethod
    def get_plugins():
        with open(".vinotes/plugins.json", "r") as data:
            return json.load(data)

    @staticmethod
    def get_plugin_config(key: str):
        with open(".vinotes/plugins.json", "r") as data:
            plugins = json.load(data)
        try:
            return plugins[key]
        except KeyError:
            raise Exception(f"cannot find plugin {key} in plugins.json")


# test the util if run as main
if __name__ == "__main__":
    test_util = Util()
    print(test_util.get_config("vim_command"))
    print(test_util.get_plugin_config())
