import operator
from functools import reduce


def knot_one(lengths: list) -> int:
    knots = list(range(256))
    cur_pos = 0
    skip_size = 0
    for length in lengths:
        end_pos = (cur_pos + length)
        if end_pos > len(knots):
            start_size = end_pos - len(knots)
            start_pos = end_pos%len(knots)
            combined = (knots[cur_pos:] + knots[:start_pos])[::-1]
            split_size = len(combined) - start_size
            knots = combined[split_size:] + knots[start_pos:cur_pos] + combined[:split_size]
        else:
            knots = knots[:cur_pos] + knots[cur_pos:end_pos][::-1] + knots[end_pos:]

        cur_pos += (length + skip_size)
        cur_pos %= len(knots)
        skip_size += 1
    return knots[0] * knots[1]


def knot_two(lengths: str) -> str:
    converted_lengths = [ord(str(x)) for x in lengths] + [17, 31, 73, 47, 23]

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

    values = [int(x) for x in value.split(",")]
    print("One - Knot Multiply:", knot_one(values))
    print("Two - Knot Hash:", knot_two(value))
