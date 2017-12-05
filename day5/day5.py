#!/usr/bin/env python

import time


def exit_maze(instructions):
    memory = [int(val) for val in instructions.split('\n')]
    i = 0
    count = 0
    while i < len(memory):
        step = memory[i]
        memory[i] += 1
        i += step
        count += 1
    return count


def exit_maze_with_check(instructions):
    memory = [int(val) for val in instructions.split('\n')]
    i = 0
    count = 0
    while i < len(memory):
        step = memory[i]
        if step >= 3:
            memory[i] -= 1
        else:
            memory[i] += 1
        i += step
        count += 1
    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    for fn in (exit_maze, exit_maze_with_check,):
        start = time.time()
        num = fn(data.strip())
        end = time.time()
        elapsed = end - start
        print('Result: {0}, time: {1}'.format(num, elapsed))
