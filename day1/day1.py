#!/usr/bin/env python

import time


def inverse_captcha(input):
    result = 0
    nums = list(input)
    for i, n in enumerate(nums):
        j = i + 1
        if j >= len(nums):
            j = 0
        if int(n) == int(nums[j]):
            result += int(n)
    return result


def inverse_captcha_halfway(input):
    assert len(input) % 2 == 0
    halfway = int(len(input) / 2)
    result = 0
    nums = list(input)
    for i, n in enumerate(nums):
        j = i + halfway
        if j >= len(nums):
            j -= len(nums)
        if int(n) == int(nums[j]):
            result += int(n)
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        captcha = f.read().strip()

    for fn in (inverse_captcha, inverse_captcha_halfway,):
        start = time.time()
        result = fn(captcha)
        end = time.time()
        diff = end - start
        print('{fn} result: {r}, time {t}'.format(fn=fn, r=result, t=diff))
