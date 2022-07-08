import json


def load_file(path):
    with open(path) as f:
        return json.load(f)
