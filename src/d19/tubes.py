directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def tubes_one(network: list) -> str:
    direction = (1, 0)
    next_coords = (0, network[0].index("|"))
    collected = []

    steps = []

    def char_at(y_x: tuple):
        return network[y_x[0]][y_x[1]]

    while True:
        next_coords = (next_coords[0] + direction[0], next_coords[1] + direction[1])
        if next_coords[0] < 0 or next_coords[0] > len(network):
            return "".join(collected)
        if next_coords[1] < 0 or next_coords[1] > len(network[next_coords[0]]):
            return "".join(collected)

        char = char_at(next_coords)
        steps.append(char)
        if char == "|" or char == "-":
            continue
        if char == "+":
            for i in range(directions.index(direction) + 1, directions.index(direction) + len(directions), 2):
                tmp_dir = directions[i % len(directions)]
                char = char_at((next_coords[0] + tmp_dir[0], next_coords[1] + tmp_dir[1]))
                if char == "-" or char == "|":
                    direction = tmp_dir
                    break
        elif char == " ":
            return "".join(collected)
        else:
            collected += char
            continue


def tubes_two(network: list) -> int:
    direction = (1, 0)
    next_coords = (0, network[0].index("|"))

    steps = []

    def char_at(y_x: tuple):
        return network[y_x[0]][y_x[1]]

    while True:
        next_coords = (next_coords[0] + direction[0], next_coords[1] + direction[1])
        if next_coords[0] < 0 or next_coords[0] > len(network):
            return len(steps)
        if next_coords[1] < 0 or next_coords[1] > len(network[next_coords[0]]):
            return len(steps)

        char = char_at(next_coords)
        steps.append(char)
        if char == "|" or char == "-":
            continue
        if char == "+":
            for i in range(directions.index(direction) + 1, directions.index(direction) + len(directions), 2):
                tmp_dir = directions[i % len(directions)]
                char = char_at((next_coords[0] + tmp_dir[0], next_coords[1] + tmp_dir[1]))
                if char == "-" or char == "|":
                    direction = tmp_dir
                    break
        elif char == " ":
            return len(steps)


if __name__ == '__main__':
    in_lines = []
    while True:
        value = input()
        if value:
            in_lines.append(value)
        else:
            break

    if not in_lines:
        with open("input.txt", "r") as f:
            in_lines = f.read().splitlines()

    print("One - Seen Letters:", tubes_one(in_lines))
    print("Two - Steps:", tubes_two(in_lines))
