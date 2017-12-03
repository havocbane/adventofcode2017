import math
import time


def spiral_memory(search):
    if search < 2:
        return 0
    grid = [0]
    block = 1
    # The diagonals are squares of primes.
    while block <= math.sqrt(search):
        # The distances range between the block number and twice the block number.
        # The first number on the block is one less than the max range.
        distance = block * 2 - 1
        stop = block * 2
        # We always generate a multiple of 8 distances.
        for i in range(8 * block):
            grid.append(distance)
            # Always start counting down.
            if i == 0:
                count_up = False
            elif distance == block:
                count_up = True
            elif distance == stop:
                count_up = False

            if count_up:
                distance += 1
            else:
                distance -= 1
        block += 1
    return grid[search - 1]


if __name__ == '__main__':
    search = 325489
    start = time.time()
    result = spiral_memory(search)
    end = time.time()
    elapsed = end - start
    print("Result {0}, time {1}".format(result, elapsed))
