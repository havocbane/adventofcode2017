#!/usr/bin/env python

from functools import reduce
import operator
import time


def knot_hash(lengths, list_size=256, cur_pos=0, skip=0, cur_list=None):
    if cur_list is None:
        cur_list = list(range(list_size))
    for k, length in enumerate(lengths):
        if length > list_size:
            raise Exception('uh oh!')
        if length > 0:
            tmp = []
            for i in range(length):
                j = (cur_pos + i) % list_size
                tmp.append(cur_list[j])
            tmp.reverse()
            for i, el in enumerate(tmp):
                j = (cur_pos + i) % list_size
                cur_list[j] = el
        if (k < list_size):
            cur_pos = (cur_pos + length + skip) % list_size
            skip += 1
    return cur_list[0] * cur_list[1], cur_list, cur_pos, skip

def hash(ascii):
    lengths = [ord(ch) for ch in ascii]
    lengths += [17, 31, 73, 47, 23]
    cur_pos = 0
    skip = 0
    sparse_hash = None
    for _ in range(64):
        _, sparse_hash, cur_pos, skip = knot_hash(lengths, cur_pos=cur_pos, skip=skip, cur_list=sparse_hash)
    dense_hash = []
    for i in range(0, len(sparse_hash), 16):
        dense_hash.append(reduce(operator.xor, sparse_hash[i:i + 16]))
    return ''.join(['{:02X}'.format(el) for el in dense_hash]).lower()


if __name__ == '__main__':
    puzzle_input = '192, 69, 168, 160, 78, 1, 166, 28, 0, 83, 198, 2, 254, 255, 41, 12'

    start = time.time()
    int_lengths = [int(el.strip()) for el in puzzle_input.split(',')]
    result = knot_hash(int_lengths)[0]
    end = time.time()
    elapsed = end - start
    print('Result: {result}, time: {elapsed}'.format(result=result, elapsed=elapsed))

    start = time.time()
    remove_whitespace = ''.join([ch.strip() for ch in puzzle_input.split()])
    result = hash(remove_whitespace)
    end = time.time()
    elapsed = end - start
    print('Result: {result}, time: {elapsed}'.format(result=result, elapsed=elapsed))
