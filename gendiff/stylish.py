import itertools


def stylish(current_value, depth=0):
    if not isinstance(current_value, dict):
        return str(current_value)
    replacer = ' '
    spaces_count = 4
    deep_indent_size = depth + spaces_count
    current_indent = replacer * depth
    deep_indent = replacer * deep_indent_size
    lines = []
    dict_ = {
        'nested': [0, ''],
        'unc': [0, ''],
        'add': [-2, '+ '],
        'rm': [-2, '- '],
        'chang': [-2, '- ', '+ ']
    }
    for key, val in current_value.items():
        if isinstance(val, list):
            format_bool_val(val)
            if val[0] == 'chang':
                lines.append(f'{deep_indent[2:]}- {key}:'
                             f' {stylish(val[1], deep_indent_size)}')
                key = f'{deep_indent[2:]}+ {key}'
                val = val[2]
            else:
                key = f'{(dict_[val[0]][0] + deep_indent_size) * replacer}' \
                      f'{dict_[val[0]][1]}{key}'
                val = val[1]
            lines.append(f'{key}: {stylish(val, deep_indent_size)}')
        else:
            lines.append(f'{deep_indent}{key}:'
                         f' {stylish(val, deep_indent_size)}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def format_bool_val(val):
    for i, v in enumerate(val):
        if v is True or v is False:
            val[i] = str(val[i]).lower()
        elif v is None:
            val[i] = 'null'
    return val
