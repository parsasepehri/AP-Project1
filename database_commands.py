import json
filename = "data.json"

def load_data():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return "error"

def save_data(data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except:
        return "error"
