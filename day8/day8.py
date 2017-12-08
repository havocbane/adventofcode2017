#!/usr/bin/env python

import ast
import operator
import time
from collections import defaultdict


ops = {
    '==': operator.eq,
    '!=': operator.ne,
    '>': operator.gt,
    '>=': operator.ge,
    '<': operator.lt,
    '<=': operator.le,
}


def compute_largest_register(data):
    instructions = data.strip().split('\n')
    registers = defaultdict(int)
    largest_seen = 0
    for row in instructions:
        values = row.split()  # e.g. ['b', 'inc', '5', 'if', 'a', '>', '1']
        register, instruction, value = values[0], values[1], int(ast.literal_eval(values[2]))
        lhs, op, rhs = values[4], values[5], int(ast.literal_eval(values[6]))
        if ops[op](registers[lhs], rhs):
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
