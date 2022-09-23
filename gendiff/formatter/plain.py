from gendiff.constants import (NESTED, ADDED, REMOVED, CHANGED)


def formatter(diff):
    return build_plain(diff)


def build_plain(diff, path=''):
    lines = []
    for key, val in diff.items():
        new_path = path + f'{key}'
        if NESTED in val:
            add = (build_plain(val[1], path + f'{key}.'))
        elif CHANGED in val:
            add = f"Property '{new_path}' was updated. From " \
                  f"{format_val(val[1:])} to {format_val(val[2:])}"
        elif ADDED in val:
            add = f"Property '{new_path}' was added with value: " \
                  f"{format_val(val[1:])}"
        elif REMOVED in val:
            add = f"Property '{new_path}' was removed"
        else:
            continue
        lines.append(add)
    return '\n'.join(lines)


def format_val(value):
    for v in value:
        if isinstance(v, dict):
            v = '[complex value]'
        elif v is True or v is False or v == 'true' or v == 'false':
            v = f'{str(v).lower()}'
        elif v is None or v == 'null':
            v = 'null'
        elif isinstance(v, int):
            v = f'{v}'
        else:
            v = f"'{v}'"
        return v
