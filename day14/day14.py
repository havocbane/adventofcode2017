#!/usr/bin/env python

import os
import sys
import time

import networkx as nx


def generate_disk(secret):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
    from day10.day10 import hash as knot_hash

    disk = []
    for i in range(128):
        k = secret + '-' + str(i)
        h = knot_hash(k)
        row = []
        for c in h:
            row.extend('{0:04b}'.format(int(c, 16)))
        disk.append(row)
    return disk


def count_squares(secret):
    disk = generate_disk(secret)
    count = 0
    for row in disk:
        for bit in row:
            if bit == '1':
                count += 1
    return count


def count_regions(secret):
    disk = generate_disk(secret)
    # Generate a full 128x128 2D lattice.
    graph = nx.generators.lattice.grid_2d_graph(128, 128)
    for x in range(128):
        for y in range(128):
            # Remove all nodes that aren't set on the disk.
            if disk[x][y] != '1':
                graph.remove_node((x, y,))
    # The number of connected groups left is our answer.
    return nx.number_connected_components(graph)


if __name__ == '__main__':
    puzzle_input = 'amgozmfv'
    for fn in (count_squares, count_regions,):
        start = time.time()
        result = fn(puzzle_input)
        end = time.time()
        elapsed = end - start
        print('Result: {result}, time: {time}'.format(result=result, time=elapsed))
