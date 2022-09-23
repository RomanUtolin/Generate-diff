import pytest
from gendiff import parsing, io

right_dict = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}


@pytest.mark.parametrize('file, format_',
                         [
                             (io.read_file("./tests/fixtures/file1.json"), 'json'),
                             (io.read_file("./tests/fixtures/file3.yml"), 'yaml')
                         ])
def test_parsing(file, format_):
    assert parsing.parse(file, format_) == right_dict
