#!/usr/bin/env python

import time


class Node(object):
    def __init__(self, value, adjacency_list):
        self.value = value
        self.adjacency_list = adjacency_list

    def __lt__(self, rhs):
        return True if self.x < rhs.x else False


def build_graph(data):
    graph = []
    root = None
    for line in data.split('\n'):
        items = line.split()
        node = Node(items[0], ''.join(items[2:]).split(','))  # ignore spaceship
        graph.append(node)
        if node.value == '0':
            root = node
    assert root is not None
    return graph, root


def dfs(graph, root, group):
    group.append(root.value)
    for node_value in root.adjacency_list:
        if node_value not in group:
            node = next(filter(lambda n: n.value == node_value, graph))
            dfs(graph, node, group)


def find_zero_group_size(data):
    graph, root = build_graph(data.strip())
    group = []
    dfs(graph, root, group)
    return len(group)

def find_number_of_groups(data):
    graph, _ = build_graph(data.strip())
    groups = []
    for node in graph:
        group = []
        dfs(graph, node, group)
        group.sort()
        if group not in groups:
            groups.append(group)
    return len(groups)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    for fn in (find_zero_group_size, find_number_of_groups,):
        start = time.time()
        result = fn(data)
        end = time.time()
        elapsed = end - start
        print('Result: {result}, time: {time}'.format(result=result, time=elapsed))
