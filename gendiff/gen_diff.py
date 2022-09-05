from collections import OrderedDict

from gendiff import open_file, stylish


def search_diff(dict_1, dict_2):
    diff = dict()
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


def generate_diff(path_1, path_2, formatter=stylish.stylish):
    dict_1 = open_file.load_file(path_1)
    dict_2 = open_file.load_file(path_2)
    diff = formatter(search_diff(dict_1, dict_2))
    return diff
