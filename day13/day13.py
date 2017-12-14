#!/usr/bin/env python

import sys
import time
from collections import defaultdict, namedtuple
from copy import copy

Level = namedtuple('Level', 'scanner direction span')
Level.__new__.__defaults__ = (None, 'down', 0)


def initialize(data):
    state = defaultdict(Level)
    for line in data.split('\n'):
        depth, span = line.strip().split(':')
        state[int(depth)] = Level(0, 'down', int(span.strip()))
    return state


def move_scanners(state):
    for index, level in state.items():
        if level.span == 0:
            continue

        direction = level.direction
        if direction == 'down':
            position = level.scanner + 1
        elif direction == 'up':
            position = level.scanner - 1

        if position == level.span - 1:
            direction = 'up'
        elif position == 0:
            direction = 'down'
        state[index] = Level(position, direction, level.span)


def packet_riding(data):
    state = initialize(data.strip())
    cur_level = 0
    max_level = max(state.keys())
    caught = 0
    while cur_level <= max_level:
        if state[cur_level].scanner == 0:
            caught += cur_level * state[cur_level].span
        cur_level += 1
        move_scanners(state)
    return caught


def run_simulation(state):
    max_level = max(state.keys())
    cur_level = 0
    while cur_level <= max_level:
        if state[cur_level].scanner == 0:
            return False
        cur_level += 1
        move_scanners(state)
    return True


def find_when_not_captured(data):
    state = initialize(data.strip())
    wait = 0
    while True:
        # Skip the first state because we would always get immediately captured.
        wait += 1
        move_scanners(state)
        if run_simulation(copy(state)):
            break
        # Brute forcing takes a long time, so show some progress.
        if wait % 100000 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
    print()
    return wait


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    for fn in (packet_riding, find_when_not_captured):
        start = time.time()
        result = fn(data)
        end = time.time()
        elapsed = end - start
        print('Result: {result}, time: {time}'.format(result=result, time=elapsed))
