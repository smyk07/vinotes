# purpose: convert config.json's data to a python dictionary,
#          and return the data requested through a function get_config()
# command: none

import os
import sys
import json

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", ".vinotes"))
)

# config
with open(".vinotes/config.json", "r") as data:
    config = json.load(data)


def get_config(key: str):
    try:
        return config[key]
    except KeyError:
        raise Exception(f"cannot find config field {key}")


# dev config
with open(".vinotes/dev.config.json", "r") as data:
    dev_config = json.load(data)


def get_dev_config(key: str):
    try:
        return dev_config[key]
    except KeyError:
        raise Exception(f"cannot find dev config field {key}")
