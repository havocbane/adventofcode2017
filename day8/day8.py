#!/usr/bin/env python

import time
from collections import defaultdict


def compute_largest_register(data):
    instructions = data.strip().split('\n')
    registers = defaultdict(int)
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
    largest_value = max(registers.values())
    return largest_value


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    start = time.time()
    largest = compute_largest_register(data.strip())
    end = time.time()
    elapsed = end - start
    print('Result: {largest}, time: {elapsed}'.format(largest=largest, elapsed=elapsed))
