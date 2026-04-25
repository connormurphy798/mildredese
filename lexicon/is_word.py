import sys
from pathlib import Path
import json

import make_dictionary

def get_definition(word, uid_df):
    uid = uid_df[uid_df['word'] == word].index[0]
    for json_file in Path("definitions").iterdir():
        with open(json_file, 'r', encoding='utf-8') as f:
            definitions = json.load(f)
            if uid in definitions:
                return definitions[uid]

def main():
    uid_df = make_dictionary.make_uid_df("uid.csv")
    is_word = sys.argv[1] in uid_df['word'].values
    if is_word:
        print(f"{sys.argv[1]} is a word.")
        definition = get_definition(sys.argv[1], uid_df)
        if 'def' in definition:
            for pos, meanings in definition['def'].items():
                print(f"{pos}:")
                for meaning in meanings:
                    print(f"  - {meaning}")
        if 'par' in definition:
            print(f"Derived from {", ".join([uid_df.loc[parent]['word'] for parent in definition['par']])}.")
    else:
        print(f"{sys.argv[1]} is not a word.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python is_word.py <word>")
        sys.exit(1)
    main()
