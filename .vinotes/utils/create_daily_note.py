#!/usr/bin/python3

# purpose: creates a daily note when run.
# command: vinotes open-daily

# import packages
import os
import sys 
from pathlib import Path
import datetime
import subprocess

# import config
from config_manager import get_config

# import templates
from template_manager import get_template

# setting date variable to name the file...
ct = datetime.datetime.now()
date = ct.strftime(get_config("date_format"))

# check for files in daily
daily_dir = get_config("daily_notes_directory")
files = os.listdir(daily_dir)

# if - file exists - create and apply template
# else - open already existing daily file
if (f"{date}.md") in files:
    pass
    subprocess.run(f"{get_config("vim_command")} {daily_dir}/{date}.md", shell=True, executable="/bin/bash")
else:
    note_path = Path(f"./{daily_dir}/{date}.md")
    with note_path.open("w") as note:
        note.write(get_template("daily", date))
    subprocess.run(f"{get_config("vim_command")} {daily_dir}/{date}.md", shell=True, executable="/bin/bash")
