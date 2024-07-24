#!/usr/bin/python3

# purpose: script for opening notes by taking in the note's path or by fuzzy finding into all of the principle directories.
# command: vn on

# import packages
import sys
import subprocess

# import config
from config_manager import get_config

# compile sys.argv
if len(sys.argv) > 2:
    tempstr = ""
    templist = []
    for i in range(0, len(sys.argv)):
        if i <= 1:
            templist.append(sys.argv[i])
        elif i >= 2:
            tempstr = f"{tempstr} {sys.argv[i]}"
    templist.append(tempstr[1:])
    args = templist
else:
    args = sys.argv

# determine path to open
if len(args) < 3:
    wd = subprocess.check_output("pwd", shell=True, executable="/bin/bash").decode(
        "utf-8"
    )[:-1]
    dirs = "".join(f"{dir} " for dir in get_config("principle_dirs"))
    try:
        file_path = subprocess.check_output(
            f"find {dirs} -type f | fzf",
            shell=True,
            executable="/bin/bash",
        ).decode("utf-8")[:-1]
    except subprocess.CalledProcessError:
        quit()
else:
    file_path = f"{args[2]}"

# open file
subprocess.run(
    f"{get_config("vim_command")} \"{file_path}\"", shell=True, executable="/bin/bash"
)
