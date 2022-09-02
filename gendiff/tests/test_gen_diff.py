from gendiff.gen_diff import generate_diff


def test_diff_json():
    result = generate_diff("./gendiff/tests/fixtures/file1.json",
                           "./gendiff/tests/fixtures/file2.json")
    with open("./gendiff/tests/fixtures/test_diff.txt") as f:
        right = f.read()
    assert result == right


def test_deep_dif_json():
    result = generate_diff("./gendiff/tests/fixtures/hard1.json",
                           "./gendiff/tests/fixtures/hard2.json")
    with open("./gendiff/tests/fixtures/test_deep_diff.txt") as f:
        right = f.read()
    assert result == right


def test_diff_yaml():
    result = generate_diff("./gendiff/tests/fixtures/file3.yml",
                           "./gendiff/tests/fixtures/file4.yml")
    with open("./gendiff/tests/fixtures/test_diff.txt") as f:
        right = f.read()
    assert result == right


def test_deep_dif_yaml():
    result = generate_diff("./gendiff/tests/fixtures/yaml1.yaml",
                           "./gendiff/tests/fixtures/yaml2.yaml")
    with open("./gendiff/tests/fixtures/test_deep_diff.txt") as f:
        right = f.read()
    assert result == right
