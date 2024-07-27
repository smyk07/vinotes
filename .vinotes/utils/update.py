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

# branch and repo url
branch = "dev"
repo_url = f"https://raw.githubusercontent.com/smyk07/vinotes/{branch}/.vinotes"

# update tracked files...

# get tracked files
with open(".vinotes/utils/tracked_files.json", "r") as data:
    files = json.load(data)

# getting and comparing file contents
for file in files:
    try:
        with urllib.request.urlopen(f"{repo_url}{file}") as response:
            remote_file_content = response.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        print(f"\n{file} has some errors: {err.code} {err.reason}")
        quit()

    present_file = Path(f".vinotes/{file}")
    present_file_content = present_file.read_text()

    if remote_file_content != present_file_content:
        print(f"{file} has updates")
    else:
        print(f"{file} does not have updates")
