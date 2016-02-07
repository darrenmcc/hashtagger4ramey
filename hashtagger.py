import sys
import random

def main(n):
    with open('/usr/share/dict/words', 'r') as f:
        hashtags = map(
            lambda word: '#' + word.strip(), 
            random.sample(f.readlines(), n)
        )

    print ' '.join(hashtags)

if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)
