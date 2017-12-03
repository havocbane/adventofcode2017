def spiral_memory(search):
    spiral = {
        '0,0': 1
    }

    right = lambda i, j: (i, j + 1,)
    up    = lambda i, j: (i - 1, j,)
    left  = lambda i, j: (i, j - 1,)
    down  = lambda i, j: (i + 1, j,)

    i = 0
    j = 1
    k = 1
    directions = [up]

    val = 1
    while val < search:
        val = find_adj(spiral, i, j)
        spiral['{i},{j}'.format(i=i, j=j)] = val

        fn = directions.pop(0)
        i, j = fn(i, j)
        if len(directions) == 0:
            k += 1
            if fn == up:
                directions.extend([left] * k)
                directions.extend([down] * k)
            if fn == down:
                directions.extend([right] * k)
                directions.extend([up] * k)
    return val


def find_adj(spiral, i, j):
    # Adjacent neighbors differ in indices by one in each direct.
    neighbor_indicies = [
        '{x},{y}'.format(x=x, y=y)
        for x, y in (
            (i, j + 1,),
            (i, j - 1,),
            (i + 1, j,),
            (i - 1, j,),
            (i + 1, j + 1,),
            (i + 1, j - 1,),
            (i - 1, j + 1,),
            (i - 1, j - 1,),
        )
    ]
    sum = 0
    for neighbor_index in neighbor_indicies:
        try:
            sum += spiral[neighbor_index]
        except KeyError:
            pass
    return sum

if __name__ == '__main__':
    print(spiral_memory(325489))
