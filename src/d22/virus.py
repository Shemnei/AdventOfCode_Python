from collections import defaultdict

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def virus_one(nodes: list) -> int:
    grid = defaultdict(lambda: ".")
    c_x, c_y = int(len(nodes[0]) / 2), int(len(nodes) / 2)
    for y, r in enumerate(nodes):
        for x, c in enumerate(r):
            if c == "#":
                grid[(x-c_x, c_y-y)] = "#"

    bursts = 10_000
    x, y = 0, 0
    direction = 0
    infected = 0
    for b in range(bursts):
        if grid[(x, y)] == "#":
            grid.pop((x, y))
            direction += 1
        else:
            grid[(x, y)] = "#"
            direction -= 1
            infected += 1
        direction %= len(directions)
        x += directions[direction][0]
        y += directions[direction][1]
    return infected


def virus_two(nodes: list) -> int:
    grid = defaultdict(lambda: ".")
    c_x, c_y = int(len(nodes[0]) / 2), int(len(nodes) / 2)
    for y, r in enumerate(nodes):
        for x, c in enumerate(r):
            if c == "#":
                grid[(x - c_x, c_y - y)] = "#"

    bursts = 10_000_000
    x, y = 0, 0
    direction = 0
    infected = 0
    for b in range(bursts):
        node = grid[(x, y)]
        if node == "#":
            grid[(x, y)] = "F"
            direction += 1
        elif node == ".":
            grid[(x, y)] = "W"
            direction -= 1
        elif node == "W":
            infected += 1
            grid[(x, y)] = "#"
        elif node == "F":
            grid.pop((x, y))
            direction += 2
        direction %= len(directions)
        x += directions[direction][0]
        y += directions[direction][1]
    return infected


if __name__ == '__main__':
    in_lines = [x for x in input() if x]
    while True:
        value = input()
        if value:
            in_lines.append(value)
        else:
            break

    if not in_lines:
        with open("input.txt", "r") as f:
            in_lines = f.read().splitlines()

    in_nodes = [list(x) for x in in_lines]

    print("One - Total Infected Cells:", virus_one(in_nodes))
    print("Two - Total Infected Cells:", virus_two(in_nodes))
