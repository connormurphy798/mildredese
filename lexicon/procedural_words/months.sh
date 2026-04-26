#!/bin/bash
# This file defines the names of the months in Mildredese, along with their associated tags and definitions.

# Define the month names and their tags
months_english=(
    "january" "february" "march" "april" "may" "june"
    "july" "august" "september" "october" "november" "december"
)
numbers_mildredese=(
    "je" "lo" "ga" "mu" "fo" "bru"
    "dve" "frhø" "zi" "ghy" "ghyje" "ghylo"
)
# Loop through the months and add them to the lexicon
for i in "${!months_english[@]}"; do
    month="${months_english[i]}"
    mildredese="njo${numbers_mildredese[i]}"
    python add_word.py -w "$mildredese" -f "definitions/time.json" -d noun "$month" -p njo "${numbers_mildredese[i]}"
done
