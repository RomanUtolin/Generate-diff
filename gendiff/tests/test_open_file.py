from gendiff import open_file


json = open_file.load_file("./gendiff/tests/fixtures/file1.json")
yaml = open_file.load_file("./gendiff/tests/fixtures/file3.yml")
right_dict = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}


def test_open_json():
    assert json == right_dict


def test_open_yaml():
    assert yaml == right_dict