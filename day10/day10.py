#!/usr/bin/env python

import time


def knot_hash(input_lengths, list_size=256):
    skip = 0
    cur_pos = 0
    l = list(range(list_size))
    lengths = [int(el.strip()) for el in input_lengths.split(',')]
    for length in lengths:
        if length > list_size:
            raise Exception('uh oh!')
        if length > 0:
            tmp = []
            for i in range(length):
                j = (cur_pos + i) % list_size
                tmp.append(l[j])
            tmp.reverse()
            for i, el in enumerate(tmp):
                j = (cur_pos + i) % list_size
                l[j] = el
        cur_pos = (cur_pos + length + skip) % list_size
        skip += 1
    return l[0] * l[1]


if __name__ == '__main__':
    puzzle_input = '192, 69, 168, 160, 78, 1, 166, 28, 0, 83, 198, 2, 254, 255, 41, 12'
    start = time.time()
    result = knot_hash(puzzle_input)
    end = time.time()
    elapsed = end - start
    print('Result: {result}, time: {elapsed}'.format(result=result, elapsed=elapsed))
