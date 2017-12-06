#!/usr/bin/env python

import time


def debugger(memory_banks):
    memory = [int(bank.strip()) for bank in memory_banks.strip().split()]
    seen = []
    configuration = ','.join([str(bank) for bank in memory])
    while configuration not in seen:
        seen.append(configuration)

        # Find the first memory bank containing the largest value and remove all data.
        largest = max(memory)
        i = memory.index(largest)
        memory[i] = 0

        # Distribute that data evenly across all cells starting at index + 1,
        # making sure to loop back around to the beginning.
        while largest > 0:
            if i == len(memory) - 1:
                i = 0
            else:
                i += 1
            memory[i] += 1
            largest -= 1
        # Update and store (at the top of the loop) the new configuration.
        configuration = ','.join([str(bank) for bank in memory])
    # Seen should contain only unique configurations.
    return len(seen)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
    for fn in (debugger,):
        start = time.time()
        num = fn(data.strip())
        end = time.time()
        elapsed = end - start
        print('Result: {0}, time: {1}'.format(num, elapsed))
