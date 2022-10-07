import json
import os

#vars
nameStorageFile = 'storage.data'

def load_json():
    with open(nameStorageFile) as json_file:
        json_dict = json.load(json_file)
    return json_dict

def save_json(json_dict):
    with open(nameStorageFile, 'w') as json_file:
        json.dump(json_dict, json_file, indent=2)

def create_json():
        with open(os.path.join(nameStorageFile), 'w') as json_file:
            json_file.write(json.dumps({}, indent = 2))

def startup_check():
    if not (os.path.isfile(nameStorageFile) or os.access(nameStorageFile, os.R_OK)):
        create_json()
    else:
        os.remove(nameStorageFile)
        create_json()

def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]