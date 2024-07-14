# purpose: provides template content to note-creating scripts.
# command: none

# import modules
import os
import sys
import datetime

# inserting to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')))

# import templates
# from <filename> import <func> as <func_name_here>

# default zettelkasten templates
from fleeting import content as fleeting
from literature import content as literature
from permanent import content as permanent
from daily import content as daily

# funcs dictionary
funcs = {
    "fleeting": fleeting, 
    "literature": literature, 
    "permanent": permanent,
    "daily": daily
}

# get timestamp
ct = datetime.datetime.now()
timestamp = f"{ct.year}-{ct.month}-{ct.day} {ct.hour}:{ct.minute}"

# manage templating
def get_template(func, filename):
    if func in funcs: 
        return funcs[func](filename, timestamp)
    else: 
        raise Exception(f"{func} not implemented, thus cant access template")
