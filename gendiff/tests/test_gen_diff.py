from gendiff.gen_diff import generate_diff


def test_generate_diff():
    result = generate_diff("./gendiff/tests/fixtures/file1.json", "./gendiff/tests/fixtures/file2.json")

    assert result == generate_diff("./gendiff/tests/fixtures/file1.json", "./gendiff/tests/fixtures/file2.json")
