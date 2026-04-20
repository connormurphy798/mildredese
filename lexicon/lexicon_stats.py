import pandas as pd
from pathlib import Path
import json
import matplotlib.pyplot as plt

import make_dictionary

CON = ['m', 'nj', 'ng', 'n', 'p', 'th', 't', 'kh', 'k', 'b', 'dh', 'd', 'gh', 'g', 'f', 's', 'v', 'z', 'rh', 'r', 'l', 'h']
SEM = ['j', 'w']
VOW = ['a', 'e', 'i', 'o', 'u', 'y', 'ø']

def get_noncompound_words(uid_file="uid.csv", directory="definitions"):
    uid_df = make_dictionary.make_uid_df(uid_file)
    lexicon_dict = {}
    for json_file in Path(directory).iterdir():
        with open(json_file, 'r', encoding='utf-8') as f:
            lexicon_dict |= json.load(f)
    noncompound_words = []
    for uid, entry in lexicon_dict.items():
        if 'par' not in entry:
            noncompound_words.append(uid_df.loc[uid]['word'])
    return sorted(noncompound_words)

def get_phonemes(word):
    phonemes = {"con1": "", "con2": "", "sem1": "", "vow": "", "sem2": ""}
    remainder = word
    for i in range(2):
        for c in CON:
            if remainder.startswith(c):
                phonemes[f"con{i+1}"] = remainder[:len(c)]
                remainder = remainder[len(c):]
                break
    for s in SEM:
        if remainder.startswith(s):
            phonemes["sem1"] = remainder[:len(s)]
            remainder = remainder[len(s):]
            break
    for v in VOW:
        if remainder.startswith(v):
            phonemes["vow"] = remainder[:len(v)]
            remainder = remainder[len(v):]
            break
    for s in ["i", "u"]:
        if remainder.startswith(s):
            phonemes["sem2"] = remainder[:len(s)]
            remainder = remainder[len(s):]
            break
    return phonemes

def plot_initial_consonant_frequencies(df):
    df['con1'].value_counts().plot.bar()
    plt.xticks(rotation=0)
    plt.show()

def plot_vowel_frequencies(df):
    df['vow'].value_counts().plot.bar()
    plt.xticks(rotation=0)
    plt.show()

def main():
    words = get_noncompound_words()
    records = []
    for word in words:
        phonemes = get_phonemes(word)
        records.append(phonemes)
    df = pd.DataFrame(records, index=words)
    print(df)
    plot_initial_consonant_frequencies(df)
    plot_vowel_frequencies(df)

if __name__ == "__main__":
    main()