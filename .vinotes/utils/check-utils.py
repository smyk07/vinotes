# purpose: when run, installs new utils, and updates existing utils
# command: vn check-utils

# import dependencies
import json
import base64
from pathlib import Path
import urllib.request
import urllib.error
from rich import print


# import templates and config
from utils.config_manager import Util as config_manager_util

get_config = config_manager_util.get_config


# write utility class
class Util:
    def __init__(self, command_args=[]) -> None:
        self.name = "check-utils"
        self.docstring = """Installs new vinotes utils, and updates existing utils."""
        self.extended_docstring = """When run, compares the utils on the main branch of vinotes' github repo with the present utils, installs any new utils, and updates present utils (only if updates exist)."""
        self.util_type = "command"
        self.command_args = command_args

    def command(self):
        # write your command here

        # thought process:
        #   compare the files inside of utils directory both here and remote
        #     create a new file if exists, delete existing file, if does not exist (in remote)
        #   compare individual files
        #     update local util file if updates are present

        created_file_count = 0
        updated_file_count = 0

        # comparing just files
        try:
            with urllib.request.urlopen(
                "https://api.github.com/repos/smyk07/vinotes/contents/.vinotes/utils?ref=dev"
            ) as response:
                remote_files = [
                    f["path"] for f in json.loads(response.read().decode("utf-8"))
                ]
        except urllib.error.HTTPError as err:
            print(f"Errors while requesting folder content: {err.code} {err.reason}")
            quit()

        present_files = [
            str(f) for f in Path("./.vinotes/utils").iterdir() if f.is_file()
        ]

        for file in remote_files:
            if file not in present_files:
                # run creation code
                file_path = Path(file)

                with file_path.open("w") as script:
                    script.write(get_remote_file_contents(util=file.split("/")[-1]))

                created_file_count += 1
                print(f"{file} - created new util")
            else:
                # run updation code
                file_path = Path(file)
                remote_file_contents = get_remote_file_contents(
                    util=file.split("/")[-1]
                )

                if file_path.read_text() != remote_file_contents:
                    with file_path.open("w") as script:
                        script.write(remote_file_contents)
                    updated_file_count += 1
                    print(f"{file} - updated util")

        print(
            f"\n[bold light_green]Utils Checked[/] - {created_file_count} utils created, {updated_file_count} utils updated."
        )
        print(
            "Run [bold light_green]vn check-plugins[/] to update Vinotes 3rd-party plugins."
        )


# function for getting file from github
def get_remote_file_contents(util: str, branch: str = "dev") -> str:
    try:
        with urllib.request.urlopen(
            f"https://api.github.com/repos/smyk07/vinotes/contents/.vinotes/utils/{util}?ref={branch}"
        ) as response:
            file_json_data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"Errors while requesting file contents: {err.code} {err.reason}")
        quit()

    return base64.b64decode(file_json_data["content"]).decode("utf-8")


# test file if run as main.
if __name__ == "__main__":
    # testing util
    # test_util = Util()
    # test_util.command()

    # testing get_file_from_github
    # print(get_file_from_github(util="changelog.py"))
    pass
