import json


def open_file(path1,path2):
    json1 = json.load(open(str(path1)))
    json2 = json.load(open(str(path2)))
    return json1, json2