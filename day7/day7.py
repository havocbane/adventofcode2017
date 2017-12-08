#!/usr/bin/env python

import time


class Program(object):
    def __init__(self, name, weight, links):
        self.name = name
        self.weight = int(weight)
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
            return name, parsed_nodes


class Tree(object):
    children = []

    def __init__(self, root, children):
        self.root = root
        self.children = children

    def get_children(self):
        return self.children

    def __repr__(self):
        return "{name} -> [{children}]".format(name=self.root, children=','.join([child.root for child in self.children]))


def find_unbalanced(data):
    root, parsed_nodes = find_root(data)

    def create_child_trees(children):
        child_trees = []
        for child in children:
            sub_children = [parsed_nodes[link] for link in child.links]
            child_trees.append(Tree(child.name, create_child_trees(sub_children)))
        return child_trees

    children = [parsed_nodes[link] for link in parsed_nodes[root].links]
    tree = Tree(root, create_child_trees(children))
    sums = {}

    def find_sums(root, children):
        total = 0
        for child in children:
            total += parsed_nodes[child.root].weight
            if child.get_children():
                total += find_sums(child.root, child.get_children())
        sums[root] = parsed_nodes[root].weight + total
        return total

    find_sums(tree.root, tree.get_children())

    def find_mismatched(root):
        child_sums = []
        for child in root.get_children():
            if child.root in sums:
                child_sums.append(sums[child.root])

        if len(set(child_sums)) <= 1:
            # We have found the bad node!
            return root

        over_weight = max(child_sums)
        i = child_sums.index(over_weight)

        mismatched_child = root.get_children()[i]
        mismatched = find_mismatched(mismatched_child)
        diff = over_weight - min(child_sums)
        if isinstance(mismatched, int):
            return mismatched
        return parsed_nodes[mismatched.root].weight - diff
    return find_mismatched(tree)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    start = time.time()
    root = find_root(data.strip())[0]
    end = time.time()
    elapsed = end - start
    print('Result: {root}, time: {elapsed}'.format(root=root, elapsed=elapsed))

    start = time.time()
    mismatched = find_unbalanced(data.strip())
    end = time.time()
    elapsed = end - start
    print('Result: {mismatched}, time: {elapsed}'.format(mismatched=mismatched, elapsed=elapsed))
