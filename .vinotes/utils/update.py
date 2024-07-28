#!/usr/bin/python3

# purpose: will update all utilities and scripts
# command: vn update

# import packages
import json
from pathlib import Path
import urllib.request
import urllib.error

# import config
from config_manager import get_config
from config_manager import get_dev_config

# quit if dev mode is enabled in config
if get_dev_config("dev_mode"):
    print(
        "\nIn dev mode, disable dev mode to update binaries, note that this can trash your current changes."
    )
    quit()

# update tracked files...
try:
    with urllib.request.urlopen(
        f"{get_dev_config("remote_raw_repo_url")}{get_dev_config("remote_raw_repo_branch")}/.vinotes/utils/tracked_files.json"
    ) as response:
        remote_tracked_files_json = response.read().decode("utf-8")
except urllib.error.HTTPError as err:
    print(f"Cannot check for tracked files: {err.code} {err.reason}")
    quit()

present_tracked_files_json = Path(".vinotes/utils/tracked_files.json")
if remote_tracked_files_json != present_tracked_files_json.read_text():
    present_tracked_files_json.write_text(remote_tracked_files_json)

# get tracked files
with open(".vinotes/utils/tracked_files.json", "r") as data:
    files = json.load(data)

# getting and comparing file contents
for file in files:
    try:
        with urllib.request.urlopen(
            f"{get_dev_config("remote_raw_repo_url")}{get_dev_config("remote_raw_repo_branch")}/.vinotes{file}"
        ) as response:
            remote_file_content = response.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        print(f"\n{file} has some errors: {err.code} {err.reason}")
        quit()

    present_file = Path(f".vinotes/{file}")

    if str(present_file).endswith(".json"):
        if present_file.is_file():
            remote_json = json.loads(remote_file_content)
            present_json = json.loads(present_file.read_text())
            if remote_json.keys() == present_json.keys():
                print(f"{file} does not have updates")
            else:
                for key, value in remote_json:
                    if key in present_json:
                        pass
                    else:
                        present_json.update({key: value})
                print(f"{file} updated")
        else:
            with present_file.open("w") as json_file:
                json_file.write(remote_file_content)
            print(f"{file} created (new file)")
    else:
        if present_file.is_file():
            if remote_file_content != present_file.read_text():
                present_file.write_text(remote_file_content)
                print(f"{file} updated")
            else:
                print(f"{file} does not have updates")
        else:
            # create new file
            with present_file.open("w") as script:
                script.write(remote_file_content)
            print(f"{file} created (new file)")
