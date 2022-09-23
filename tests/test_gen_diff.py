import pytest
from gendiff.gen_diff import generate_diff


def read_file(file):
    with open(file) as f:
        return f.read()


@pytest.mark.parametrize("right_file,file_1,file_2,formatter",
                         [
                             ("./tests/fixtures/right_stylish_diff.txt", "./tests/fixtures/hard1.json",
                              "./tests/fixtures/yaml2.yaml", 'stylish',),
                             ("./tests/fixtures/right_plain_diff.txt", "./tests/fixtures/hard1.json",
                              "./tests/fixtures/yaml2.yaml", 'plain'),
                             ("./tests/fixtures/right_json_diff.txt", "./tests/fixtures/hard1.json",
                              "./tests/fixtures/yaml2.yaml", 'json')

                         ])
def test_diff(file_1, file_2, formatter, right_file):
    assert read_file(right_file) == generate_diff(file_1, file_2, formatter)
