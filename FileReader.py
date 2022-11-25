import re
from pathlib import Path


def JsonReader(self):
    with open(self, "r") as raw:
        json_raw = raw.read()
    return json_raw


pass


class reader:

    def read_file(self):
        file = re.findall('(?<=\#).*', self)
        return file

    pass


path = Path("C:\\Users\\Jaco Laas\\PycharmProjects\\FileReader\\specialJson.json")
raw = JsonReader(path)
file = reader.read_file(raw)
print(file)
print(type(file))
