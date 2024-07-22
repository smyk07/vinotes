#!/usr/bin/python3

# purpose: updates the index.md file in root directory of vault every time
#          vn open command is run.

# every time this file is run:

# update index.md (default values, can be changed in config)
#   with: 5 latest daily files,
#         5 latest created files
#         display a quote
# ----------------------------------------------------------

# import modules
import subprocess
import os
from pathlib import Path
from config_manager import get_config
from quote_manager import get_quote
from template_manager import get_template

# set index.md path
index_path = Path("./index.md")

# define head of daily files
daily_files = os.listdir(f"./{get_config("daily_notes_directory")}")
daily_files.reverse()
daily_head = ""
if len(daily_files) >= 5:
    daily_files = daily_files[0:5]
for i in daily_files:
    daily_head = f"{
        daily_head}- [{i[:10]}](./{get_config("daily_notes_directory")}/{i})\n"

# write template to index.md
with index_path.open("w") as index:
    index.write(get_template("index", "index.md", get_quote(), daily_head))

# open index.md
subprocess.run(
    f"{get_config("vim_command")} index.md", shell=True, executable="/bin/bash"
)
