#!/usr/bin/python3

# purpose: when run, opens the config.json file in nano.
# command: vinotes conf

import subprocess

subprocess.run("nano .vinotes/config.json", shell=True, executable="/bin/bash")
