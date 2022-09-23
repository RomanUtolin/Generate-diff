import itertools
from gendiff.constants import (NESTED, UNCHANGED, ADDED, REMOVED, CHANGED)

NEW_REPLACER = {
    NESTED: '  ',
    UNCHANGED: '  ',
    ADDED: '+ ',
    REMOVED: '- ',
    CHANGED: ['- ', '+ ']
}


def formatter(diff):
    return do_format(diff)


def value_add(lines, key, val, depth):
    lines.append(f'{key}: {do_format(val, depth)}')
    return lines


def format_bool_val(item):
    for i, val in enumerate(item):
        if val is True or val is False:
            item[i] = str(val).lower()
        elif val is None:
            item[i] = 'null'


def do_format(diff, depth=0):
    if not isinstance(diff, dict):
        return diff
    replacer = ' '
    spaces_count = 4
    deep_indent_size = depth + spaces_count
    deep_indent = replacer * deep_indent_size
    lines = []
    for key, val in diff.items():
        if isinstance(val, list):
            state = val[0]
            format_bool_val(val)
            new_indent = deep_indent[2:]
            if state == CHANGED:
                add_key = f'{new_indent}{NEW_REPLACER[CHANGED][0]}{key}'
                add_val = val[1]
                value_add(lines, add_key, add_val, deep_indent_size)
                add_key = f'{new_indent}{NEW_REPLACER[CHANGED][1]}{key}'
                add_val = val[2]
            else:
                new_replacer = NEW_REPLACER[state]
                add_key = f'{new_indent}{new_replacer}{key}'
                add_val = val[1]
            value_add(lines, add_key, add_val, deep_indent_size)
        else:
            add_key = f'{deep_indent}{key}'
            add_val = val
            value_add(lines, add_key, add_val, deep_indent_size)
    result = itertools.chain("{", lines, [replacer * depth + "}"])
    return '\n'.join(result)
