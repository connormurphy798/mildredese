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
    with open(f'dictionary/{word[0]}/{word}.md', 'w', encoding='utf-8') as f:
        f.write(f"# {word}\n\n")
        if 'par' in entry:
            parents = [uid_df.loc[parent_uid]['word'] for parent_uid in entry['par']]
            compound = ", ".join(f"[{parent}](../{parent[0]}/{parent}.md)" for parent in parents)
            f.write(f"\ncompound of {compound}\n\n")
        for pos in entry['def']:
            f.write(f"\n_{pos}_\n\n")
            for definition in entry['def'][pos]:
                f.write(f"- {definition}\n")
        

if __name__ == "__main__":
    make_dictionary_folders()

    uid_df = pd.read_csv('uid.csv', header=None, names=['word'], index_col=1)
    print(uid_df)
    # lexicon_files = ['pronouns.json', 'lexicon.json']
    count = 0
    for filename in Path('definitions').iterdir():
        with open(filename, 'r', encoding='utf-8') as f:
            lexicon_dict = json.load(f)
            for uid in lexicon_dict:
                word = uid_df.loc[uid]['word']
                write_md(word, uid, lexicon_dict, uid_df)
                count += 1
    print(f"Wrote {count} entries to dictionary.")
    with open('dictionary/index.md', 'w', encoding='utf-8') as f:
        f.write("# Temiudred lexicon\n\n")
        for filename in Path('dictionary').iterdir():
            if filename.is_dir():
                for md_file in filename.iterdir():
                    if md_file.suffix == '.md':
                        word = md_file.stem
                        f.write(f"- [{word}]({filename.name}/{md_file.name})\n")

        