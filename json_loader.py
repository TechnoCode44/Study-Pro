from json import load, dump

def load_json(filename):
    try:
        file = open(filename)
        json = load(file)
        return json
    except FileNotFoundError:
        return None

def save_json(dictionary, filename):
    with open(filename, "w", encoding="utf-8") as file:
        dump(dictionary, file, ensure_ascii=False, indent=4)