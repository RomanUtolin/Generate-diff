from collections import OrderedDict

from gendiff import open_file
from gendiff.formatter import stylish, plain, json

formatter = {
    'stylish': stylish,
    'plain': plain,
    'json': json
}


def format_bool_val(current_dict):
    for key, val in current_dict.items():
        if val is True or val is False:
            current_dict[key] = str(val).lower()
        elif val is None:
            current_dict[key] = 'null'


def search_diff(dict_1, dict_2):
    diff = dict()
    format_bool_val(dict_1)
    format_bool_val(dict_2)
    dict_1_keys = set(dict_1.keys())
    dict_2_keys = set(dict_2.keys())
    intersection_keys = (dict_1_keys.intersection(dict_2_keys))
    for key in intersection_keys:
        value_1 = dict_1[key]
        value_2 = dict_2[key]
        if isinstance(value_1, dict) and isinstance(value_2, dict):
            diff[key] = ['nested', search_diff(value_1, value_2)]
        elif value_1 == value_2:
            diff[key] = ['unc', value_1]
        else:
            diff[key] = ['chang', value_1, value_2]
    removed = dict_1_keys.difference(dict_2_keys)
    for key in removed:
        diff[key] = ['rm', dict_1[key]]
    added = dict_2_keys.difference(dict_1_keys)
    for key in added:
        diff[key] = ['add', dict_2[key]]
    return OrderedDict(sorted(diff.items()))


def generate_diff(path_1, path_2, format_='stylish'):
    dict_1 = open_file.load_file(path_1)
    dict_2 = open_file.load_file(path_2)
    diff = search_diff(dict_1, dict_2)
    return formatter[format_].formatter(diff)
