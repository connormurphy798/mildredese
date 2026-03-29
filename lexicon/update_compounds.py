from pathlib import Path
import json
import in_place
import sys

import make_dictionary

def help():
    print("\nUsage:\n")
    print("To update a word and all compounds that contain it:")
    print("\tpython update_compounds.py <word_to_modify> <modified_word>")
    print("\nTo do the above and update dictionary:")
    print("\tpython update_compounds.py <word_to_modify> <modified_word> --update-dictionary")

def identify_compounds(uid_df):
    uid_word_dict = {}
    uid_parent_dict = {}
    for uid, row in uid_df.iterrows():
        word = row['word']
        uid_word_dict[uid] = word
        uid_parent_dict[uid] = []

    for filename in Path('definitions').iterdir():
        with open(filename, 'r', encoding='utf-8') as f:
            lexicon_dict = json.load(f)
            for uid in lexicon_dict:
                if 'par' in lexicon_dict[uid]:
                    for parent_uid in lexicon_dict[uid]['par']:
                        uid_parent_dict[uid].append(parent_uid)
    # for uid, parents in uid_parent_dict.items():
    #     if parents:
    #         print(f"{uid}: {parents} ({uid_word_dict[uid]}: {[uid_word_dict[parent] for parent in parents]})")
    return {uid: parents for uid, parents in uid_parent_dict.items() if parents}, uid_word_dict

def modify_compounds(modified_uid, modified_word, uid_parent_dict, uid_word_dict):
    uid_word_dict[modified_uid] = modified_word
    modified_uids = {modified_uid}
    num_modified_uids = 0
    while len(modified_uids) > num_modified_uids:
        num_modified_uids = len(modified_uids)
        for uid, parents in uid_parent_dict.items():
            to_add = False
            for modified_uid in modified_uids:
                if modified_uid in parents:
                    to_add = True
            if to_add:
                modified_uids.add(uid)
                uid_word_dict[uid] = ''.join(uid_word_dict[parent] for parent in parents)
    return uid_word_dict

def update_csv(uid_word_dict):
    with in_place.InPlace('uid.csv', encoding='utf-8') as f:
        first_line = True
        for line in f:
            word, uid = line.strip().split(',')
            f.write(f"{'\n' if not first_line else ''}{uid_word_dict[uid]},{uid}")
            first_line = False

def main():
    if len(sys.argv) < 3:
        help()
        exit(1)
    word_to_modify, modified_word = sys.argv[1], sys.argv[2]
    if len(sys.argv) == 3:
        update_dictionary = False
    elif len(sys.argv) == 4 and sys.argv[3] in ('--update-dictionary', '-u'):
        update_dictionary = True
    else:
        help()
        exit(1)
    
    uid_df = make_dictionary.make_uid_df()
    modified_uid = uid_df[uid_df['word'] == word_to_modify].index[0]
    uid_parent_dict, uid_word_dict = identify_compounds(uid_df)
    uid_word_dict[modified_uid] = modified_word
    uids_word_dict = modify_compounds(modified_uid, modified_word, uid_parent_dict, uid_word_dict)
    update_csv(uid_word_dict)

    if update_dictionary:
        make_dictionary.remove_dictionary_entries()
        make_dictionary.make_dictionary()

if __name__ == "__main__":
    main()
    # print(identify_compounds())
    # print(identify_modified_compounds("49mwSlQd", identify_compounds()))
    
    