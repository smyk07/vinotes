#!/usr/bin/python3

# purpose: creates a note by taking in the directory's name and the filename to create
#          and then will create a file with the given name inside of the directory
#          specified and apply the template specific to the directory.
# command: vinotes create-note <path/to/note>

# import packages
import sys
from pathlib import Path
import subprocess

# import templates and config
from template_manager import get_template
from config_manager import get_config

# combining filepath into a single list element
if len(sys.argv) >= 3:
    args = []
    tempstr = ""
    for i in range(0, len(sys.argv)):
        if i <= 1:
            args.append(sys.argv[i])
        elif i >= 2:
            tempstr = f"{tempstr} {sys.argv[i]}"
    args.append(tempstr[1:])
else:
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

# create file variable
file = Path(f"./{file_path}.md")


# define function for opening note, as its repeated below in 2 cases...
def open_with_editor(vim_command, file_path):
    subprocess.run(
        f'{vim_command} "{file_path}.md"',
        shell=True,
        executable="/bin/bash",
    )


# if - file exists, do not create and quit.
# else - create file, apply template.
if file.is_file():
    print()
    print(f"{file_name}.md exists in {file_path}")
    open_note = input("Open note? (Y/n): ")
    if open_note == "y" or open_note == "":
        open_with_editor(get_config("vim_command"), file_path)
else:
    try:
        temp_data = get_template(template, file_name)
        dir_path.mkdir(parents=True, exist_ok=True)
        with file.open("w") as note:
            note.write(temp_data)
        if get_config("open_note_when_created"):
            open_with_editor(get_config("vim_command"), file_path)
    except ModuleNotFoundError:
        print("Cannot create file, template not found")
        quit()
