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
from pathlib import Path
from quote_manager import get_quote
from template_manager import get_template

index_path = Path("./index.md")

with index_path.open("w") as index:
    index.write(get_template("index", "index.md", get_quote()))
