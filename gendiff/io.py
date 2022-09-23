def read_file(item):
    return open(item)


def get_format(item):
    if item.endswith('.yml') or item.endswith('.yaml'):
        file_format = 'yaml'
    else:
        file_format = 'json'
    return file_format
