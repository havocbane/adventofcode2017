#!/usr/bin/env python

import time
from collections import defaultdict, namedtuple

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


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    for fn in (packet_riding,):
        start = time.time()
        result = fn(data)
        end = time.time()
        elapsed = end - start
        print('Result: {result}, time: {time}'.format(result=result, time=elapsed))
