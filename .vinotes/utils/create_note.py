#!/usr/bin/python3

# purpose: creates a note by taking in the directory's name and the filename to create
#          and then will create a file with the given name inside of the directory
#          specified and apply the template specific to the directory.
# command: vinotes create-note <path/to/note>

# import packages
import sys
from pathlib import Path
import subprocess

# import templates
from template_manager import get_config, get_template

# assignment of arguments to variable
args = sys.argv

# construct filename into a single list element
if len(args) > 3:
    templist = []
    tempstr = ""
    for i in range(0, len(args)):
        if i <= 1:
            templist.append(args[i])
        elif i >= 2:
            tempstr = f"{tempstr} {args[i]}"
    templist.append(tempstr[1:])
    args = templist
elif len(args) < 3:
    print()
    print("Please enter a path to your note")
    print("Correct usage:")
    print("vinotes create <path/to/note>")
    quit()

# split path to note
file_path = args[2]
path_split = file_path.split("/")
template = path_split[0]
file_name = path_split[len(path_split) - 1]

# if given directory == daily, print message and quit.
if template == "daily":
    print()
    print("Please use open-daily, od command within vinotes")
    print("to create a daily note.")
    quit()

# create directories if they dont exist
dirstring = ""
if len(path_split) > 1:
    for i in range(0, len(path_split)):
        if i < len(path_split) - 1:
            dirstring = f"{dirstring}/{path_split[i]}"
dir_path = Path(f".{dirstring}")
dir_path.mkdir(parents=True, exist_ok=True)

# create file variable
file = Path(f"./{file_path}.md")

# if - file exists, do not create and quit.
# else - create file, apply template.
if file.is_file():
    print()
    print(f"{file_name}.md exists in {file_path}")
    open_file = input("Open file? (Y/n): ")
    if open_file == "y" or open_file == "":
        subprocess.run(
            f"{get_config("vim_command")} ./{file_path}.md",
            shell=True,
            executable="/bin/bash",
        )
else:
    with file.open("w") as note:
        note.write(get_template(template, file_name))
    open_file = get_config("open_note_when_created")
    if open_file:
        subprocess.run(
            f"{get_config("vim_command")} ./{file_path}.md",
            shell=True,
            executable="/bin/bash",
        )
