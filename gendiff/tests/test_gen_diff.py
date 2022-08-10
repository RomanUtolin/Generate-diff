from gendiff.gen_diff import generate_diff


def test_generate_diff_json():
    result = generate_diff("./gendiff/tests/fixtures/file1.json",
                           "./gendiff/tests/fixtures/file2.json")
    with open("./gendiff/tests/fixtures/plain.txt") as f:
        right = f.read()
    assert result == right


def test_generate_diff_yaml():
    result = generate_diff("./gendiff/tests/fixtures/file3.yml",
                           "./gendiff/tests/fixtures/file4.yml")
    with open("./gendiff/tests/fixtures/plain.txt") as f:
        right = f.read()
    assert result == right
