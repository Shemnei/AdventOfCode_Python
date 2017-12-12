import operator

direction = {"n": (0, 1, -1), "ne": (1, 0, -1), "se": (1, -1, 0), "s": (0, -1, 1), "sw": (-1, 0, 1), "nw": (-1, 1, 0)}


def hex_one(directions: list) -> int:
    coords = (0, 0, 0)
    for d in directions:
        coords = tuple(map(operator.add, coords, direction[d]))
    return int((abs(coords[0]) + abs(coords[1]) + abs(coords[2])) / 2)


def hex_two(directions: list) -> int:
    max_dist = 0
    coords = (0, 0, 0)
    for d in directions:
        coords = tuple(map(operator.add, coords, direction[d]))
        dist = int((abs(coords[0]) + abs(coords[1]) + abs(coords[2])) / 2)
        if max_dist < dist:
            max_dist = dist
    return max_dist


if __name__ == '__main__':
    value = input()

    if not value:
        with open("input.txt", "r") as f:
            value = f.read()

    values = value.split(",")
    print("One - Hex Steps Away:", hex_one(values))
    print("Two - Max Steps Away:", hex_two(values))
