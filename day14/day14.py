#!/usr/bin/env python

import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from day10.day10 import hash as knot_hash


def generate_disk(secret):
    disk = []
    for i in range(128):
        k = secret + '-' + str(i)
        h = knot_hash(k)
        disk.append('{:0<128b}'.format(int(h, 16)))
    return disk


def count_used_squares(secret):
    disk = generate_disk(secret)
    count = 0
    for row in disk:
        for bit in row:
            if bit == '1':
                count += 1
    return count


if __name__ == '__main__':
    puzzle_input = 'amgozmfv'
    start = time.time()
    result = count_used_squares(puzzle_input)
    end = time.time()
    elapsed = end - start
    print('Result: {result}, time: {time}'.format(result=result, time=elapsed))
