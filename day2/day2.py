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


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        dat = f.read()
    start = time.time()
    result = checksum(dat)
    end = time.time()
    elapsed = end - start
    print("Result: {0}, time {1}".format(result, elapsed))
