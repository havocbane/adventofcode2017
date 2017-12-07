#!/usr/bin/env python

import time


class Program(object):
    def __init__(self, name, weight, links):
        self.name = name
        self.weight = weight
        self.links = links

    def __repr__(self):
        program_links = ', '.join(self.links) if self.links else ''
        return "{name} ({weight}) -> [{links}]".format(name=self.name, weight=self.weight, links=program_links)


def parse_nodes(data):
    programs = {}
    lines = data.split('\n')
    for line in lines:
        items = line.strip().split()
        name = items[0]
        weight = items[1][1:-1]  # remove parens
        links = [neighbor[:-1] if neighbor[-1] == ',' else neighbor for neighbor in items[3:]]  # skip the arrow, remove commas
        programs[name] = Program(name, weight, links)
    return programs


def find_root(data):
    parsed_nodes = parse_nodes(data)
    depths = {node: 0 for node in parsed_nodes.keys()}

    def find_depths(nodes):
        for name, node in nodes.items():
            if node.links:
                depths[name] += 1
                inner_nodes = {link: parsed_nodes[link] for link in node.links}
                find_depths(inner_nodes)

    find_depths(parsed_nodes)

    # The root node will be 1, all children will be > 1 except leaves which stay at 0
    for name, depth in depths.items():
        if depth == 1:
            return name


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    start = time.time()
    root = find_root(data.strip())
    end = time.time()
    elapsed = end - start
    print('Result: {root}, time: {elapsed}'.format(root=root, elapsed=elapsed))
