import json
import yaml


def open_file(file, file_format):
    if file_format == '.yaml':
        return yaml.safe_load(file)
    return json.load(file)
