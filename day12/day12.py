#!/usr/bin/env python

import time


class Node(object):
    def __init__(self, value, adjacency_list):
        self.value = value
        self.adjacency_list = adjacency_list


def build_graph(data):
    graph = []
    root = None
    for line in data.split('\n'):
        items = line.split()
        node = Node(items[0], ''.join(items[2:]).split(','))  # ignore spaceship
        graph.append(node)
        if node.value == '0':
            root = node
    return graph, root


def find_zero_group_size(data):
    def dfs(graph, root):
        zero_group.append(root.value)
        for node_value in root.adjacency_list:
            if node_value not in zero_group:
                node = next(filter(lambda n: n.value == node_value, graph))
                dfs(graph, node)

    graph, root = build_graph(data.strip())
    assert root is not None

    zero_group = []
    dfs(graph, root)
    return len(zero_group)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    start = time.time()
    result = find_zero_group_size(data)
    end = time.time()
    elapsed = end - start
    print('Result: {result}, time: {time}'.format(result=result, time=elapsed))
