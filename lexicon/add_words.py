import random
import string
import sys
import json

import user_input

def uid(n):
    """Generate a random alphanumeric string of length n."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def help():
    print("Usage:")
    print("\tpython add_words.py # generate a random alphanumeric string of length 8")
    print("\tpython add_words.py <word_1> <word_2> ... <word_n> # generate n (word, string) pairs")
    print("\tpython add_words.py -w <word_1> <word_2> ... <word_n> # generate n (word, string) pairs and write to uid.csv")

def write_definition(uid, pos, definition, file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    data[uid] = {"def": {pos: definition}}
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    if len(sys.argv) == 1:
        print(uid(8))
    # elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
    #     help()
    #     return
    # elif sys.argv[1] == '--write' or sys.argv[1] == '-w':
    #     with open('uid.csv', 'a') as f:
    #         print(f"wrote:")
    #         for word in sys.argv[2:]:
    #             id = uid(8)
    #             f.write(f"\n{word},{id}")
    #             print(f"{word},{id}")
    #         print("to uid.csv")
    # else:
    #     for word in sys.argv[1:]:
    #         print(f"{word},{uid(8)}")
    tags = [("--help", "-h"), ("--write", "-w"), ("--file", "-f"), ("--define", "-d")]
    tag_data = user_input.organize_tags(tags, sys.argv) # user_input.organize tags always records long tag
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
        help()
        return
    if "--write" in tag_data:
        if not tag_data["--write"]:
            print("Error: --write requires at least one argument.")
            exit(1)
        with open('uid.csv', 'a') as f:
            print(f"wrote:")
            for word in tag_data["--write"]:
                word_uid = uid(8)
                f.write(f"\n{word},{word_uid}")
                print(f"\t{word},{word_uid}")
            print("to uid.csv")
    if "--file" in tag_data:
        if "--write" not in tag_data:
            print("Error: --file requires --write to specify the output file.")
            exit(1)
        if len(tag_data["--file"]) != 1:
            print("Error: --file requires exactly one argument.")
            exit(1)
        if "--define" not in tag_data:
            print("Error: --file requires --define to specify the word definition.")
            exit(1)
        # TODO: write function to write to json file in addition to csv
    if "--define" in tag_data:
        if not tag_data["--define"]:
            print("Error: --define requires at least one argument.")
            exit(1)
        if "--write" not in tag_data:
            print("Error: --define requires --write to specify a word.")
            exit(1)
        if "--file" not in tag_data:
            print("No output file specified. Writing to definitions/uncategorized.json")
            def_file = "definitions/uncategorized.json"
        if len(tag_data["--define"]) != 2:
            print("Error: --define requires exactly two arguments: a part of speech and a definition (in quotes if multiple words).")
            exit(1)
        pos = tag_data["--define"][0]
        definition = tag_data["--define"][1]
        write_definition(word_uid, pos, definition, def_file)
    



if __name__ == "__main__":
    main()
