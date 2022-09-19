import itertools

NEW_REPLACER = {
    'nested': '  ',
    'unc': '  ',
    'add': '+ ',
    'rm': '- ',
}


def value_add(list_, key, val, depth):
    list_.append(f'{key}: {stylish(val, depth)}')
    return list_


def stylish(value, depth=0):
    if not isinstance(value, dict):
        return value
    replacer = ' '
    spaces_count = 4
    deep_indent_size = depth + spaces_count
    deep_indent = replacer * deep_indent_size
    lines = []
    for key, val in value.items():
        if isinstance(val, list):
            new_indent = deep_indent[2:]
            if 'chang' in val:
                add_key = f'{new_indent}{NEW_REPLACER["rm"]}{key}'
                add_val = val[1]
                value_add(lines, add_key, add_val, deep_indent_size)
                add_key = f'{new_indent}{NEW_REPLACER["add"]}{key}'
                add_val = val[2]
            else:
                new_replacer = NEW_REPLACER[val[0]]
                add_key = f'{new_indent}{new_replacer}{key}'
                add_val = val[1]
            value_add(lines, add_key, add_val, deep_indent_size)
        else:
            add_key = f'{deep_indent}{key}'
            add_val = val
            value_add(lines, add_key, add_val, deep_indent_size)
    result = itertools.chain("{", lines, [replacer * depth + "}"])
    return '\n'.join(result)
