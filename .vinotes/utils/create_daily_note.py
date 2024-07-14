#!/usr/bin/python3

# purpose: creates a daily note when run.
# command: vinotes open-daily

# import packages
import os
import sys 
from pathlib import Path
import datetime
import subprocess

# setting date variable to name the file...
ct = datetime.datetime.now()
date = ct.strftime("%Y-%m-%d")

# check for files in daily
files = os.listdir("daily/")

# if - file exists - create and apply template
# else - open already existing daily file
if (f"{date}.md") in files:
    pass
    subprocess.run(f"nvim daily/{date}.md", shell=True, executable="/bin/bash")
else:
    note_path = Path(f"./daily/{date}.md")
    with note_path.open("w") as note:
        from template_manager import get_template
        note.write(get_template("daily", date))
    subprocess.run(f"nvim daily/{date}.md", shell=True, executable="/bin/bash")
