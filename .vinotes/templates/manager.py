# import templates
# from <filename> import <func> as <func_name_here>
from fleeting import content as fleeting

# funcs dictionary
funcs = {
    "fleeting": fleeting
}

# get timestamp
import datetime
ct = datetime.datetime.now()
timestamp = f"{ct.year}-{ct.month}-{ct.day} {ct.hour}:{ct.minute}"

# manage templating
def content(func, filename):
    if func in funcs: 
        return funcs[func](filename, timestamp)
    else: 
        raise Exception(f"{func} not implemented, thus cant access template")
