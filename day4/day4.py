#!/usr/bin/env python

import time


def valid_passphrases(data):
    num_valid = 0
    for line in data.split('\n'):
        words = line.split()
        if not words:
            continue
        if len(words) == len(set(words)):
            num_valid += 1
    return num_valid


def valid_passphrases_anagrams(data):
    num_valid = 0
    for line in data.split('\n'):
        words = line.split()
        if not words:
            continue
        sorted_words = []
        for word in words:
            sorted_words.append(''.join(sorted(word)))
        if len(words) == len(set(sorted_words)):
            num_valid += 1
    return num_valid


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    for fn in (valid_passphrases, valid_passphrases_anagrams,):
        start = time.time()
        num = fn(data)
        end = time.time()
        elapsed = end - start
        print('Result: {0}, time: {1}'.format(num, elapsed))
