#!/usr/bin/python3

# purpose: creates a note by taking in the directory's name and the filename to create
#          and then will create a file with the given name inside of the directory
#          specified and apply the template specific to the directory.
# command: vinotes create-note <folder> <filename>

# import packages
import sys
from pathlib import Path

# import templates
from template_manager import get_template

# assignment of arguments to variable
args = sys.argv

# if - there are spaces between the file name, concatenate them into 1 string item and
#      return a args list of only 3 elements always
# elif - theres less than 3 arguments, quit and display correct usage.
if len(args) > 4:
    templist = []
    tempstr = ""
    for i in range(0, len(args)):
        if i <= 2:
            templist.append(args[i])
        elif i >= 3:
            tempstr = f"{tempstr} {args[i]}"
    templist.append(tempstr[1:])
    args = templist
elif len(args) < 4:
    print()
    print("2 arguments needed, got less or more than 2 ")
    print("Correct usage:")
    print("vinotes create <folder> <filename>")
    quit()

# if given directory == daily, print message and quit.
if args[2] == "daily":
    print()
    print("Please use open-daily, od command within vinotes")
    print("to create a daily note.")
    quit()

# create file variable
file = Path(f"./{args[2]}/{args[3]}.md")

# if - file exists, do not create and quit.
# else - create file, apply template.
if file.is_file():
    print()
    print(f"{args[3]}.md exists in {args[2]}")
else:
    with file.open("w") as note:
        note.write(get_template(args[2], args[3]))
