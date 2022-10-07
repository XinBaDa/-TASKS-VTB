import argparse
import json
import os

# TODO 'который мог быть'
# type for value (сейчас строго str)
# проверка load_json_file -> exit 1

#vars
nameStorageFile = 'storage.data'

def main():
    args = parse_args()
    startup_check(nameStorageFile)

    with open(nameStorageFile) as json_file:
        json_dict = json.load(json_file)

    if args.all:
        print(json.dumps(json_dict, indent = 2))
    elif args.value:
        for val in args.value:
            set_key(json_dict, args.key, val)
        with open(nameStorageFile, 'w') as json_file:
            json.dump(json_dict, json_file, indent = 2)
    else:
        print(json.dumps({args.key: json_dict.get(args.key)}, indent = 2))
        

def parse_args():
    parser = argparse.ArgumentParser(
    prog='storage.py',
    description='Key-Value Storage')
    grKey = parser.add_mutually_exclusive_group(required=True)
    grKey.add_argument ('-k', '--key', type=str)
    grKey.add_argument ('-a', '--all', action='store_const', const=True, help='show all pairs key-value')
    parser.add_argument ('-v', '--value', nargs='+')
    return (parser.parse_args())

def startup_check(fileName):
    if (os.path.isfile(fileName) or os.access(fileName, os.R_OK)) == False:
        with open(os.path.join(fileName), 'w') as json_file:
            json_file.write(json.dumps({}, indent = 2))

def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]

main()