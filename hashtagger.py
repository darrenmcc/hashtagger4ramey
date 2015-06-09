import sys
import random

def main():
    with open('dictionary.txt', 'r') as f:
        word_list = f.readlines()
        n = int(sys.argv[1])
        chosen = random.sample(word_list, n)
        chosen = map(append_hashtag, chosen)
        print ', '.join(chosen)

def append_hashtag(word):
    return '#' + word.strip()

if __name__ == '__main__':
    main()