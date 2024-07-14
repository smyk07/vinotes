# purpose: convert config.json's data to a python dictionary, 
#          and return the data requested through a function get_config()
# command: none

import os, sys, json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', ".vinotes")))

config = None

with open(".vinotes/config.json", "r") as data:
    config = json.load(data)

def get_config(key: str):
    try: 
        return config[key]
    except: 
        raise Exception("config error...")
