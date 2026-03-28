from pathlib import Path
import pandas as pd
import json

def make_dictionary_folders():
    Path('dictionary').mkdir(exist_ok=True)
    for folder in ['a', 'b', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'r', 's', 't',
                    'u', 'v', 'w', 'y', 'z', 'ø']:
        Path(f'dictionary/{folder}').mkdir(exist_ok=True)

def write_md(word, uid, lexicon_dict, uid_df):
    entry = lexicon_dict[uid]
    with open(f'dictionary/{word[0]}/{word}.md', 'w') as f:
        f.write(f"# {word}\n\n")
        if 'par' in entry:
            parents = [uid_df.loc[parent_uid]['word'] for parent_uid in entry['par']]
            compound = ", ".join(f"[{parent}](../{parent[0]}/{parent}.md)" for parent in parents)
            f.write(f"\ncompound of {compound}\n\n")
        f.write(f"{entry['pos']}\n\n")
        f.write("**definition(s):**\n")
        for definition in entry['def']:
            f.write(f"- {definition}\n")
        

if __name__ == "__main__":
    make_dictionary_folders()

    uid_df = pd.read_csv('uid.csv', header=None, names=['word'], index_col=1)
    print(uid_df)
    lexicon_files = ['lexicon.json']
    with open('lexicon.json', 'r') as f:
        lexicon_dict = json.load(f)
        for uid in lexicon_dict:
            word = uid_df.loc[uid]['word']
            print(word)
            write_md(word, uid, lexicon_dict, uid_df)

        