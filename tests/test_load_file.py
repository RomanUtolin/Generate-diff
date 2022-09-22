import pytest
from gendiff import loader

json = loader.load_file("./tests/fixtures/file1.json")
yaml = loader.load_file("./tests/fixtures/file3.yml")
right_dict = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}


@pytest.mark.parametrize("test_input,expected", [(json, right_dict), (yaml, right_dict)])
def test_open_file(test_input, expected):
    assert test_input == expected
