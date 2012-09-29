import json

class GetterDict(dict):
    def __getattr__(self, a):
        return self.get(a, None)

class Config(GetterDict):
    def __init__(self, filename):
        values = json.load(open(filename, 'r'))
        self.update(values)
        super(Config, self).__init__()

