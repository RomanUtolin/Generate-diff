def formatter(value, path=''):
    lines = []
    for key, val in value.items():
        new_path = path + f'{key}'
        if 'nested' in val:
            add = (formatter(val[1], path + f'{key}.'))
        elif 'chang' in val:
            add = f"Property '{new_path}' was updated. From " \
                  f"{format_val(val[1:])} to {format_val(val[2:])}"
        elif 'add' in val:
            add = f"Property '{new_path}' was added with value: " \
                  f"{format_val(val[1:])}"
        elif 'rm' in val:
            add = f"Property '{new_path}' was removed"
        else:
            continue
        lines.append(add)
    return '\n'.join(lines)


def format_val(value):
    for v in value:
        if isinstance(v, dict):
            v = '[complex value]'
        elif v == 'true' or v == 'false' or v == 'null':
            v = f"{v}"
        else:
            v = f"'{v}'"
        return v
