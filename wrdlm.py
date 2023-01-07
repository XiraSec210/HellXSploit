import itertools

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

min_length = 6
max_length = 30

filename = 'Wordlist.txt'
with open(filename, 'w') as f:
    for n in range(min_length, max_length+1):
        for xs in itertools.product(chars, repeat=n):
            f.write(''.join(xs) + '\n') 