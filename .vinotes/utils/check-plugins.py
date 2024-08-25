# purpose: checks, installs, and updates vinotes 3rd-party plugins.
# command: describe the command

# import dependencies
from pathlib import Path
import urllib.request
import urllib.error
from rich import print


# import templates and config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config
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

        for plugin, data in plugins_from_config.items():
            for util in data["utils"]:
                if Path(f"./.vinotes/utils/{util}.py").is_file():
                    try:
                        with urllib.request.urlopen(
                            get_raw_url(plugin=data["plugin"], filename=f"{util}.py")
                        ) as response:
                            remote_file_content = response.read().decode("utf-8")
                    except urllib.error.HTTPError as err:
                        print(f"\n{util} has some errors: {err.code} {err.reason}")
                        quit()

                    util_path = Path(f"./.vinotes/utils/{util}.py")

                    if util_path.read_text() != remote_file_content:
                        with util_path.open("w") as script:
                            script.write(remote_file_content)
                            updated_count += 1
                            print(f"[cyan]{util}[/] - utility updated")
                else:
                    try:
                        with urllib.request.urlopen(
                            get_raw_url(plugin=data["plugin"], filename=f"{util}.py")
                        ) as response:
                            remote_file_content = response.read().decode("utf-8")
                    except urllib.error.HTTPError as err:
                        print(f"\n{util} has some errors: {err.code} {err.reason}")
                        quit()

                    with Path(f"./.vinotes/utils/{util}.py").open("w") as script:
                        script.write(remote_file_content)
                        created_count += 1
                        print(f"[cyan]{util}[/] - utility created")

        print(
            f"\n[light_green]Plugins Checked[/light_green] - {created_count} created, {updated_count} updated."
        )


# write helper functions here (delete the code below obv)
def get_raw_url(plugin: str, filename: str, branch: str = "main"):
    return f"https://raw.githubusercontent.com/{plugin}/{branch}/{filename}"


# test file if run as main.
if __name__ == "__main__":
    pass  # testing code goes here.
