import itertools

NEW_REPLACER = {
    'nested': '  ',
    'unc': '  ',
    'add': '+ ',
    'rm': '- ',
}


def format_bool_val(val):
    for i, v in enumerate(val):
        if v is True or v is False:
            val[i] = str(val[i]).lower()
        elif v is None:
            val[i] = 'null'
    return val


def stylish(current_value, depth=0):
    if not isinstance(current_value, dict):
        return str(current_value)
    replacer = ' '
    spaces_count = 4
    deep_indent_size = depth + spaces_count
    deep_indent = replacer * deep_indent_size
    lines = []
    for key, val in current_value.items():
        if isinstance(val, list):
            format_bool_val(val)
            if 'chang' in val:
                add_key = f'{deep_indent[2:]}- {key}'
                lines.append(f'{add_key}: {stylish(val[1], deep_indent_size)}')
                add_key = f'{deep_indent[2:]}+ {key}'
                val = val[2]
            else:
                add_key = f'{deep_indent[2:]}{NEW_REPLACER[val[0]]}{key}'
                val = val[1]
            lines.append(f'{add_key}: {stylish(val, deep_indent_size)}')
        else:
            lines.append(f'{deep_indent}{key}:'
                         f' {stylish(val, deep_indent_size)}')
    result = itertools.chain("{", lines, [replacer * depth + "}"])
    return '\n'.join(result)
