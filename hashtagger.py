import sys
import random

def main(n):
    with open('dictionary.txt', 'r') as f:
        hashtags = map(
            ht_format, 
            random.sample(f.readlines(), n)
        )

    print ', '.join(hashtags)

def ht_format(word):
    return '#' + word.strip()

if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)