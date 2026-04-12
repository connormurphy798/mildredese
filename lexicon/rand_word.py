import random
import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python rand_word.py <number>")
        sys.exit(1)
    if len(sys.argv) == 2:
        try:
            num_words = int(sys.argv[1])
        except ValueError:
            print("Argument must be an integer.")
            sys.exit(1)
    elif len(sys.argv) == 1:
        num_words = 1
    with open("../syllables.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for _ in range(num_words):
            random_line = random.choice(lines)
            print(random_line.strip())