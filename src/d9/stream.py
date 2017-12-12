def stream_one(stream: str) -> int:
    level = 0
    added_sum = 0
    ignore = False
    garbage = False
    for char in stream:
        if ignore:
            ignore = False
        elif char == "!":
            ignore = True
        elif char == "<":
            garbage = True
        elif char == ">":
            garbage = False
        elif garbage:
            pass
        elif char == "{":
            level += 1
        elif char == "}":
            added_sum += level
            level -= 1
    return added_sum


def stream_two(stream: str) -> int:
    count = 0
    ignore = False
    garbage = False
    for char in stream:
        if ignore:
            ignore = False
        elif char == "!":
            ignore = True
        elif char == ">":
            garbage = False
        elif garbage:
            count += 1
        elif char == "<":
            garbage = True
    return count


if __name__ == '__main__':
    value = input()

    if not value:
        with open("input.txt", "r") as f:
            value = f.read()

    print("One - Bracket Level Sum:", stream_one(value))
    print("Two - Garbage Count:", stream_two(value))
