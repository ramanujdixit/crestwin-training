import json


def load_file():
    with open("notes_details.json", "r") as f:
        data = json.load(f)

    return data


def save_data(data):
    with open("notes_details.json", "w") as f:
        json.dump(data, f)
