#!/usr/bin/env python

import time


def checksum(data):
    lines = data.split('\n')
    result = 0
    for row in lines:
        row = row.strip()
        if not row:
            continue
        row_vals = [int(el) for el in row.split()]
        low = min(row_vals)
        high = max(row_vals)
        result += high - low
    return result


def checksum_evenly_divided(data):
    lines = data.split('\n')
    result = 0
    for row in lines:
        row = row.strip()
        if not row:
            continue
        row_vals = [int(el) for el in row.split()]
        result += compare_row(row_vals)
    return result


def compare_row(row_vals):
    for x in row_vals:
        for y in row_vals:
            if x == y:
                continue
            if x > y:
                numer, denom = x, y
            else:
                numer, denom = y, x
            if numer % denom == 0:
                return int(numer / denom)
    raise Exception("uh oh!")


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        dat = f.read()
    for fn in (checksum, checksum_evenly_divided,):
        start = time.time()
        result = fn(dat)
        end = time.time()
        elapsed = end - start
        print("Result: {0}, time {1}".format(result, elapsed))
