#!/usr/bin/env python

import time


class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def find_z(x, y):
    # x + y + z = 0
    return 0 - x - y


def distance(p1, p2):
    return max(abs(p2.x - p1.x), abs(p2.y - p1.y), abs(p2.z - p1.z))


fn = {
    'n':  lambda x, y: (x - 1, y + 1,),
    'ne': lambda x, y: (x,     y + 1,),
    'se': lambda x, y: (x + 1, y,),
    's':  lambda x, y: (x + 1, y - 1,),
    'sw': lambda x, y: (x,     y - 1,),
    'nw': lambda x, y: (x - 1, y,),
}


def shortest_path(walk):
    p1 = Point(0, 0, 0)
    p2 = Point(0, 0, 0)
    furthest = 0
    for direction in walk:
        p2.x, p2.y = fn[direction](p2.x, p2.y)
        p2.z = find_z(p2.x, p2.y)
        furthest = max(distance(p2, p1), furthest)
    return distance(p2, p1), furthest


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    start = time.time()
    shortest_path, furthest = shortest_path(data.strip().split(','))
    end = time.time()
    elapsed = end - start
    print('Result: {shortest_path}, {furthest}, time: {elapsed}'.format(
          shortest_path=shortest_path, furthest=furthest, elapsed=elapsed))
