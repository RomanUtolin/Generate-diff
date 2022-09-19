from gendiff.gen_diff import generate_diff
from gendiff import stylish, plain


def test_diff_json_stylish():
    result = generate_diff("./gendiff/tests/fixtures/file1.json",
                           "./gendiff/tests/fixtures/file2.json",
                           stylish.stylish)
    with open("./gendiff/tests/fixtures/test_nested_diff.txt") as f:
        right = f.read()
    assert result == right


def test_diff_json_plain():
    result = generate_diff("./gendiff/tests/fixtures/file1.json",
                           "./gendiff/tests/fixtures/file2.json",
                           plain.plain)
    with open("./gendiff/tests/fixtures/test_plain_diff.txt") as f:
        right = f.read()
    assert result == right


def test_deep_dif_json_stylish():
    result = generate_diff("./gendiff/tests/fixtures/hard1.json",
                           "./gendiff/tests/fixtures/hard2.json",
                           stylish.stylish)
    with open("./gendiff/tests/fixtures/test_deep_nested_diff.txt") as f:
        right = f.read()
    assert result == right


def test_deep_diff_json_plain():
    result = generate_diff("./gendiff/tests/fixtures/hard1.json",
                           "./gendiff/tests/fixtures/hard2.json",
                           plain.plain)
    with open("./gendiff/tests/fixtures/test_deep_plain_diff.txt") as f:
        right = f.read()
    assert result == right


def test_diff_yaml_stylish():
    result = generate_diff("./gendiff/tests/fixtures/file3.yml",
                           "./gendiff/tests/fixtures/file4.yml",
                           stylish.stylish)
    with open("./gendiff/tests/fixtures/test_nested_diff.txt") as f:
        right = f.read()
    assert result == right


def test_diff_yaml_plain():
    result = generate_diff("./gendiff/tests/fixtures/file3.yml",
                           "./gendiff/tests/fixtures/file4.yml",
                           plain.plain)
    with open("./gendiff/tests/fixtures/test_plain_diff.txt") as f:
        right = f.read()
    assert result == right


def test_deep_dif_yaml_stylish():
    result = generate_diff("./gendiff/tests/fixtures/yaml1.yaml",
                           "./gendiff/tests/fixtures/yaml2.yaml",
                           stylish.stylish)
    with open("./gendiff/tests/fixtures/test_deep_nested_diff.txt") as f:
        right = f.read()
    assert result == right


def test_deep_dif_yaml_plain():
    result = generate_diff("./gendiff/tests/fixtures/yaml1.yaml",
                           "./gendiff/tests/fixtures/yaml2.yaml",
                           plain.plain)
    with open("./gendiff/tests/fixtures/test_deep_plain_diff.txt") as f:
        right = f.read()
    assert result == right
