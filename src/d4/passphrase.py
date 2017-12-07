from collections import Counter


def passphrase_one(lines: list) -> int:
    count = 0
    for li in lines:
        parts = li.split()
        set_parts = set(parts)
        if len(parts) == len(set_parts):
            count += 1
    return count


def passphrase_two(lines: list) -> int:
    count = 0
    for li in lines:
        parts = [''.join(sorted(x)) for x in li.split()]
        set_parts = set(parts)
        if len(parts) == len(set_parts):
            count += 1
    return count


if __name__ == '__main__':
    in_lines = []
    while True:
        line = input()
        if line:
            in_lines.append(line)
        else:
            break

    if not in_lines:
        with open("input.txt", "r") as f:
            in_lines = f.read().splitlines()

    print("Valid Passphrases (One):", passphrase_one(in_lines))
    print("Valid Passphrases (Two):", passphrase_two(in_lines))
