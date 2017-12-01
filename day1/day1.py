#!/usr/bin/env python


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


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        captcha = f.read().strip()
    print('Result: {}'.format(inverse_captcha(captcha)))
