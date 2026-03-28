import random
import string
import sys
from bidict import bidict

def uid(n):
    """Generate a random alphanumeric string of length n."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def help():
    print("Usage:")
    print("\tpython uid.py # generate a random alphanumeric string of length 8")
    print("\tpython uid.py <word_1> <word_2> ... <word_n> # generate n (word, string) pairs")

def main():
    if len(sys.argv) == 1:
        print(uid(8))
    elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
        help()
        return
    elif sys.argv[1] == '--write' or sys.argv[1] == '-w':
        with open('uid.csv', 'a') as f:
            print(f"wrote:")
            for word in sys.argv[2:]:
                f.write(f"\n{word},{uid(8)}")
                print(f"{word},{uid(8)}")
            print("to uid.csv")
    else:
        for word in sys.argv[1:]:
            print(f"{word},{uid(8)}")

if __name__ == "__main__":
    main()
