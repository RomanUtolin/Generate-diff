import pytest
from gendiff.gen_diff import generate_diff

with open("./tests/fixtures/right_stylish_diff.txt") as file_1:
    right_stylish = file_1.read()

with open("./tests/fixtures/right_plain_diff.txt") as file_2:
    right_plain = file_2.read()

with open("./tests/fixtures/right_json_diff.txt") as file_3:
    right_json = file_3.read()

stylish = generate_diff("./tests/fixtures/hard1.json", "./tests/fixtures/yaml2.yaml")
plain = generate_diff("./tests/fixtures/hard1.json", "./tests/fixtures/yaml2.yaml", 'plain')
json = generate_diff("./tests/fixtures/hard1.json", "./tests/fixtures/yaml2.yaml", 'json')


@pytest.mark.parametrize("test_input,expected", [(stylish, right_stylish), (plain, right_plain), (json, right_json)])
def test_diff_formatter(test_input, expected):
    assert test_input == expected
