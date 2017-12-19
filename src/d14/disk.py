import operator
from functools import reduce


def disk_one(key: str) -> int:
    size = 128
    used = 0

    for i in range(size):
        _hash = generate_hash(key + "-" + str(i))
        bin_hash = bin(int(_hash, 16))[2:]
        used += bin_hash.count("1")

    return used


def disk_two(key: str) -> int:
    size = 128
    groups = 0

    disk = []

    for i in range(size):
        _hash = generate_hash(key + "-" + str(i))
        bin_hash = bin(int(_hash, 16))[2:].zfill(size)
        disk.append([int(x) for x in bin_hash])

    for y in range(size):
        for x in range(len(disk[y])):
            if disk[y][x] == 1:
                groups += 1
                flip_group(disk, (y, x))

    return groups


def flip_group(disk: list, node: tuple):
    if node[0] < 0 or node[0] >= len(disk):
        return
    if node[1] < 0 or node[1] >= len(disk[node[0]]):
        return
    if disk[node[0]][node[1]] == 0:
        return
    disk[node[0]][node[1]] = 0
    flip_group(disk, (node[0]+1, node[1]))
    flip_group(disk, (node[0]-1, node[1]))
    flip_group(disk, (node[0], node[1]-1))
    flip_group(disk, (node[0], node[1]+1))


# day 10 - knot_two
def generate_hash(hash_key: str) -> str:
    converted_lengths = [ord(str(x)) for x in hash_key] + [17, 31, 73, 47, 23]

    knots = list(range(256))
    cur_pos = 0
    skip_size = 0

    for x in range(64):
        for length in converted_lengths:
            end_pos = (cur_pos + length)
            if end_pos > len(knots):
                start_size = end_pos - len(knots)
                start_pos = end_pos % len(knots)
                combined = (knots[cur_pos:] + knots[:start_pos])[::-1]
                split_size = len(combined) - start_size
                knots = combined[split_size:] + knots[start_pos:cur_pos] + combined[:split_size]
            else:
                knots = knots[:cur_pos] + knots[cur_pos:end_pos][::-1] + knots[end_pos:]

            cur_pos += (length + skip_size)
            cur_pos %= len(knots)
            skip_size += 1

    chunks = [reduce(operator.xor, knots[i:i + 16], 0) for i in range(0, len(knots), 16)]
    hsh = [format(x, "x").zfill(2) for x in chunks]
    return "".join(hsh)


if __name__ == '__main__':
    value = input()

    if not value:
        with open("input.txt", "r") as f:
            value = f.read()

    print("One - Used Spaces:", disk_one(value))
    print("Two - Regions:", disk_two(value))
