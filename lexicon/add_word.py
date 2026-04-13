import random
import string
import sys
import json
from pathlib import Path

import user_input

def uid(n):
    """Generate a random alphanumeric string of length n."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def help():
    print("Usage:")
    print("\tpython add_words.py # generate a random alphanumeric string of length 8")
    print("\tpython add_words.py <word_1> <word_2> ... <word_n> # generate n (word, string) pairs")
    print("\tpython add_words.py -w <word_1> <word_2> ... <word_n> # generate n (word, string) pairs and write to uid.csv")

def write_definition(uid, pos, definition, parents, file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    data[uid] = {"def": {pos: [definition]}}
    if parents:
        data[uid]["par"] = parents
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def make_uid_dict():
    uid_dict = {}
    with open('uid.csv', 'r', encoding='utf-8') as f:
        for line in f:
            word, uid = line.strip().split(',')
            uid_dict[word] = uid
    return uid_dict

def handle_errors(tag_data, uid_dict):
    if "--default" in tag_data:
        print("Error: unrecognized arguments:", " ".join(tag_data["--default"]))
        exit(1)
    if "--help" in tag_data:
        if tag_data["--help"]:
            print("Error: --help does not take any arguments.")
            exit(1)
        if len(tag_data) > 1:
            print("Error: --help cannot be used with other tags.")
            exit(1)
    if "--write" in tag_data:
        if len(tag_data["--write"]) != 1:
            print("Error: --write requires exactly one argument.")
            exit(1)
    if "--define" in tag_data:
        if not tag_data["--define"]:
            print("Error: --define requires at least one argument.")
            exit(1)
        if "--write" not in tag_data:
            print("Error: --define requires --write to specify a word.")
            exit(1)
        if len(tag_data["--define"]) != 2:
            print("Error: --define requires exactly two arguments: a part of speech and a definition (in quotes if multiple words).")
            exit(1)
    if "--file" in tag_data:
        if "--write" not in tag_data:
            print("Error: --file requires --write to specify the output file.")
            exit(1)
        if len(tag_data["--file"]) != 1:
            print("Error: --file requires exactly one argument.")
            exit(1)
        if not Path(tag_data["--file"][0]).is_file():
            print(f"Error: file {tag_data['--file'][0]} does not exist.")
            exit(1)
        if "--define" not in tag_data:
            print("Error: --file requires --define to specify the word definition.")
            exit(1)
    if "--parents" in tag_data:
        if len(tag_data["--parents"]) < 2:
            print("Error: --parents requires at least two arguments.")
            exit(1)
        if "--define" not in tag_data:
            print("Error: --parents requires --define to specify word definition.")
            exit(1)
        if "".join(tag_data["--parents"]) != tag_data["--write"][0]:
            print("Error: --parents must compound to produce the word specified by --write.")
            exit(1)
        for parent in tag_data["--parents"]:
            if parent not in uid_dict:
                print(f"Error: parent word {parent} not found in uid.csv.")
                exit(1)
    

def main():
    if len(sys.argv) == 1:
        print(uid(8))
    tags = [("--help", "-h"), ("--write", "-w"), ("--define", "-d"), ("--file", "-f"), ("--parents", "-p")]
    tag_data = user_input.organize_tags(tags, sys.argv) # user_input.organize tags always records long tag
    uid_dict = make_uid_dict()
    handle_errors(tag_data, uid_dict)

    if "--help" in tag_data:
        help()
        return

    if "--write" in tag_data:
        with open('uid.csv', 'a', encoding='utf-8') as f:
            print(f"wrote:")
            for word in tag_data["--write"]:
                word_uid = uid(8)
                f.write(f"\n{word},{word_uid}")
                print(f"\t{word},{word_uid}")
            print("to uid.csv")

    if "--file" in tag_data:
        def_file = tag_data["--file"][0]
    else:
        def_file = "definitions/uncategorized.json"

    if "--parents" in tag_data:
        parents = [uid_dict[parent] for parent in tag_data["--parents"]]
    else:
        parents = []

    if "--define" in tag_data:
        pos = tag_data["--define"][0]
        definition = tag_data["--define"][1]
        write_definition(word_uid, pos, definition, parents, def_file)

    

    

if __name__ == "__main__":
    main()
