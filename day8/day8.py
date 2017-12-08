#!/usr/bin/env python

import time
from collections import defaultdict


def compute_largest_register(data):
    instructions = data.strip().split('\n')
    registers = defaultdict(int)
    largest_seen = 0
    for row in instructions:
        values = row.split()
        register, instruction, value = values[0], values[1], int(values[2])
        conditional = 'registers["' + values[4] + '"] ' + ' '.join(values[5:])  # ignore 'if'
        modify = eval(conditional)
        if modify:
            if instruction == 'inc':
                registers[register] += value
            elif instruction == 'dec':
                registers[register] -= value
        cur_largest = max(registers.values())
        if cur_largest > largest_seen:
            largest_seen = cur_largest
    return cur_largest, largest_seen


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    start = time.time()
    largest_at_end, largest_seen = compute_largest_register(data.strip())
    end = time.time()
    elapsed = end - start
    print('Result: {largest_at_end}, largest seen: {largest_seen}, time: {elapsed}'.format(
        largest_at_end=largest_at_end, largest_seen=largest_seen, elapsed=elapsed))
