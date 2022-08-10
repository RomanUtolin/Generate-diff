from gendiff import open_file


def generate_diff(path1, path2):
    file1 = open_file.load_file(path1)
    file2 = open_file.load_file(path2)
    file1_keys = list(file1.keys())
    file2_keys = list(file2.keys())
    set_keys = sorted(list(set(file1_keys + file2_keys)))
    result = dict()
    for i in set_keys:
        if i in file1_keys and i in file2_keys:
            if file1[i] == file2[i]:
                result['  ' + i] = file1[i]
            else:
                result['- ' + i] = file1[i]
                result['+ ' + i] = file2[i]
        if i in file1_keys and i not in file2_keys:
            result['- ' + i] = file1[i]
        if i in file2_keys and i not in file1_keys:
            result['+ ' + i] = file2[i]

    result_str = ['{']
    for key, item in result.items():
        if item is False or True:
            result_str.append(f'{key}: {str(item).lower()}')
        else:
            result_str.append(f'{key}: {item}')
    result_str.append('}')
    diff = '\n'.join(result_str)
    return diff
