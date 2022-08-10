import json
import yaml


def load_file(path):
    with open(path) as f:
        if path.endswith('.yml') or path.endswith('.yaml'):
            return yaml.safe_load(f)
        return json.load(f)
