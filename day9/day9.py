#!/usr/bin/env python

import time


def stream_score(data):
    score = 0
    current_group = 0
    inside_garbage = False
    skip_next = False
    for stream in data.strip().split('\n'):
        for char in stream.strip():
            if skip_next:
                skip_next = False
            elif char == '!':
                skip_next = True
            elif inside_garbage:
                if char == '>':
                    inside_garbage = False
            elif char == '{':
                current_group += 1
            elif char == '}':
                score += current_group
                current_group -= 1
            elif char == '<':
                inside_garbage = True
    return score


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    start = time.time()
    score = stream_score(data)
    end = time.time()
    elapsed = end - start
    print('Result: {score}, time: {elapsed}'.format(score=score, elapsed=elapsed))
