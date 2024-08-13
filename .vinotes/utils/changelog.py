#!/usr/bin/python3

# purpose: when run, opens CHANGELOG.md in vim.
# command: vn changelog

# import packages
from pathlib import Path
import subprocess

# import config
from config_manager import get_config

# changelog path
changelog = Path("./CHANGELOG.md")

# checking if path exists, then opening
if changelog.is_file():
    subprocess.run(
        f"{get_config('vim_command')} \"{str(changelog)}\"",
        shell=True,
        executable=f"{get_config('shell_executable')}",
    )
else:
    print("\nFile CHANGELOG.md not found...")
