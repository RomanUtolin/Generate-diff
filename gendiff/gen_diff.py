from gendiff import open_file


def generate_diff(path1, path2):
    file1 = open_file.load_file(path1)
    file2 = open_file.load_file(path2)
    file1_keys = list(file1.keys())
    file2_keys = list(file2.keys())
    set_keys = sorted(list(set(file1_keys + file2_keys)))
    result = ['{']
    for i in set_keys:
        if i in file1_keys and i in file2_keys:
            if file1[i] == file2[i]:
                result.append(f'  {i}: {file1[i]}')
            else:
                result.append(f'- {i}: {file1[i]}')
                result.append(f'+ {i}: {file2[i]}')
        if i in file1_keys and i not in file2_keys:
            result.append(f'- {i}: {file1[i]}')
        if i in file2_keys and i not in file1_keys:
            result.append(f'+ {i}: {file2[i]}')
    result.append('}')

    return ('\n'.join(result)).lower()


path1 = "./tests/fixtures/file1.json"
path2 = "./tests/fixtures/file2.json"
print(generate_diff(path1, path2))
