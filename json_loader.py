from json import load

def load_json(filename):
    file = open(filename)
    json = load(file)
    return json