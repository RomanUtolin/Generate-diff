from gendiff import io


def load_file(item):
    with open(item) as file:
        if item.endswith('.yml') or item.endswith('.yaml'):
            file_format = '.yaml'
        else:
            file_format = '.json'
        return io.open_file(file, file_format)
