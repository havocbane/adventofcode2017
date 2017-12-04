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


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    start = time.time()
    num = valid_passphrases(data)
    end = time.time()
    elapsed = end - start
    print('Result: {0}, time: {1}'.format(num, elapsed))
