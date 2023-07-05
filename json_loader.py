from json import load, dump

def load_json(filename):
    file = open(filename)
    json = load(file)
    return json

def save_json(dictionary, filename):
    with open(filename, "w", encoding="utf-8") as file:
        dump(dictionary, file, ensure_ascii=False, indent=4)