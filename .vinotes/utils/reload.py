#!/usr/bin/python3

# purpose: reloads the vault, checks on templates and principle directories
# command: vinotes reload

# import packages
from pathlib import Path

# import principle directories from config
from config_manager import get_config

dirs_from_config = get_config("principle_dirs")
dirs_from_config.append("daily")
dirs_from_config.sort()

# checking principle directories
vault_path = Path("./")

dirs = vault_path.iterdir()
dirs = [
    str(f) for f in dirs if f.is_dir() and str(f) != ".git" and str(f) != ".vinotes"
]
dirs.sort()

# checking templates
templates_path = Path("./.vinotes/templates")

templates = templates_path.iterdir()
templates = [
    str(f).split("/")[2].split(".py")[0]
    for f in templates
    if f.is_file() and str(f) != ".vinotes/templates/example.py"
]

# Thought process:
#   consider config as the only validator
#   first check if templates exist according to config
#   then check if directories exist according to config
#       handle unknown templates and directories

for i in dirs_from_config:
    if i not in templates:
        create_template = input(
            f"\nTemplate for {i} does not exist, create a simple template? (Y/n):"
        )
        if create_template == "y" or create_template == "":
            src_template = Path(".vinotes/templates/example.py")
            dest_template = Path(f".vinotes/templates/{i}.py")
            dest_template.write_text(src_template.read_text())

    if i not in dirs:
        create_dir = input(
            f"\nPrinciple directory {i} does not exist, create directory? (Y/n):"
        )
        if create_dir == "y" or create_dir == "":
            dir_path = Path(f"./{i}")
            try:
                dir_path.mkdir(parents=False, exist_ok=True)
            except FileNotFoundError:
                print("Please do not include '/' in parent directory name.")
                print("Update .vinotes/config.json and reload again.")
                quit()

print("\nReload complete\n")
