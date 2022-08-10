from gendiff import open_file

result = open_file.load_file("./gendiff/tests/fixtures/file1.json")
right_dict = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}


def test_open_file():
    assert result == right_dict
