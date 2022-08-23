import itertools


def stylish(value):
    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        replacer = ' '
        spaces_count = 4
        deep_indent_size = depth + spaces_count
        current_indent = replacer * depth
        deep_indent = replacer * deep_indent_size
        lines = []
        for key, val in current_value.items():
            if isinstance(val, list):
                for i, v in enumerate(val):
                    if v is True:
                        val[i] = 'true'
                    elif v is None:
                        val[i] = 'null'
                    elif v is False:
                        val[i] = 'false'
                if val[0] == 'nested' or val[0] == 'unc':
                    lines.append(f'{deep_indent}{key}:'
                                 f' {walk(val[1],deep_indent_size)}')
                elif val[0] == 'add':
                    lines.append(f'{deep_indent[2:]}+ {key}:'
                                 f' {walk(val[1], deep_indent_size)}')
                elif val[0] == 'rm':
                    lines.append(f'{deep_indent[2:]}- {key}:'
                                 f' {walk(val[1], deep_indent_size)}')
                elif val[0] == 'chang':
                    lines.append(f'{deep_indent[2:]}- {key}:'
                                 f' {walk(val[1], deep_indent_size)}')
                    lines.append(f'{deep_indent[2:]}+ {key}:'
                                 f' {walk(val[2], deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}:'
                             f' {walk(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walk(value, 0)
