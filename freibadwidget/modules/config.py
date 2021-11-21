import json

"""
Load and return configuration from json file
"""

file_name = "config.json"

config = None

with open(file_name) as configfile:

    config = json.loads(configfile.read())
