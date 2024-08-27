# purpose: checks, installs, and updates vinotes 3rd-party plugins.
# command: vn check-plugins

# import dependencies
from pathlib import Path
import urllib.request
import urllib.error
from rich import print
import json
import base64


# import templates and config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config
dump_plugin_config = config_manager_util.dump_plugin_config
plugins_from_config = config_manager_util.get_plugins()


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "check-plugins"
        self.docstring = """Checks plugins.json, installs newly added plugins, and checks for updates within already-existing plugins."""
        # completely optional:
        # self.extended_docstring = """"""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        # write your command here
        # pass

        # for every plugin entry
        #     for every util within plugin
        #         if exists, check for update, if available, update, else pass
        #         if does not exist, install, else pass
        updated_count = 0
        created_count = 0

        for plugin, plugin_data in plugins_from_config.items():
            for util in plugin_data["utils"]:
                if Path(f"./.vinotes/utils/{util}.py").is_file():
                    remote_file_content = get_remote_plugin_file(
                        plugin=plugin, filename=f"{util}.py"
                    )
                    util_path = Path(f"./.vinotes/utils/{util}.py")

                    if util_path.read_text() != remote_file_content:
                        with util_path.open("w") as script:
                            script.write(remote_file_content)
                            updated_count += 1
                            print(f"[cyan]{util}[/] - utility updated")
                else:
                    remote_file_content = get_remote_plugin_file(
                        plugin=plugin, filename=f"{util}.py"
                    )

                    with Path(f"./.vinotes/utils/{util}.py").open("w") as script:
                        script.write(remote_file_content)
                        created_count += 1
                        print(f"[cyan]{util}[/] - utility created")

        print(
            f"\n[light_green]Plugins Checked[/light_green] - {created_count} created, {updated_count} updated."
        )


# function to get code from remote
def get_remote_plugin_file(plugin: str, filename: str, branch: str = "main"):
    try:
        with urllib.request.urlopen(
            f"https://api.github.com/repos/{plugin}/contents/{filename}?ref={branch}"
        ) as response:
            file_json_data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(
            f"Errors while fetching file {filename} from {plugin}: {err.code} {err.reason}"
        )
        quit()

    return base64.b64decode(file_json_data["content"]).decode("utf-8")


# test file if run as main.
if __name__ == "__main__":
    print(
        get_remote_plugin_file(
            plugin="smyk07/vinotes-demo-plugin", filename="vinotes-demo-plugin.py"
        )
    )
    pass  # testing code goes here.
