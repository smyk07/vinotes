#!/usr/bin/python3

# purpose: creates a daily note when run.
# command: vinotes open-daily

# import packages
from pathlib import Path
import datetime
import subprocess

# import config
from config_manager import get_config

# import templates
from template_manager import get_template

# setting date variable to name the file...
date = datetime.datetime.now().strftime(get_config("date_format"))

# setting daily notes directory variable
daily_dir = get_config("daily_notes_directory")
daily_dir_path = Path(daily_dir)

# create file variable
file = Path(f"./{daily_dir}/{date}.md")

# if - file exists - create and apply template
# else - open already existing daily file
if file.is_file():
    subprocess.run(
        f"{get_config("vim_command")} {daily_dir}/{date}.md",
        shell=True,
        executable="/bin/bash",
    )
else:
    temp_data = get_template("daily", date)
    if not temp_data:
        print("Cannot create file, template not found")
        quit()
    else:
        daily_dir_path.mkdir(parents=True, exist_ok=True)
        with file.open("w") as note:
            note.write(temp_data)
        subprocess.run(
            f"{get_config("vim_command")} ./{daily_dir}/{date}.md",
            shell=True,
            executable="/bin/bash",
        )
