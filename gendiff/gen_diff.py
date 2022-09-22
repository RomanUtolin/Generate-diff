from collections import OrderedDict

from gendiff import loader
from gendiff.formatter import stylish, plain, json

formatter = {
    'stylish': stylish,
    'plain': plain,
    'json': json
}


def build_diff(dict_1, dict_2):
    diff = dict()
    dict_1_keys = set(dict_1.keys())
    dict_2_keys = set(dict_2.keys())
    intersection_keys = (dict_1_keys.intersection(dict_2_keys))
    for key in intersection_keys:
        value_1 = dict_1[key]
        value_2 = dict_2[key]
        if isinstance(value_1, dict) and isinstance(value_2, dict):
            diff[key] = ['NESTED', build_diff(value_1, value_2)]
        elif value_1 == value_2:
            diff[key] = ['UNCHANGED', value_1]
        else:
            diff[key] = ['CHANGED', value_1, value_2]
    removed = dict_1_keys.difference(dict_2_keys)
    for key in removed:
        diff[key] = ['REMOVED', dict_1[key]]
    added = dict_2_keys.difference(dict_1_keys)
    for key in added:
        diff[key] = ['ADDED', dict_2[key]]
    return OrderedDict(sorted(diff.items()))


def generate_diff(path_1, path_2, format_='stylish'):
    dict_1 = loader.load_file(path_1)
    dict_2 = loader.load_file(path_2)
    diff = build_diff(dict_1, dict_2)
    return formatter[format_].formatter(diff)
