from collections import defaultdict

import math


def circus_one(lines: list) -> str:
    bad = set()
    words = set()

    for line in lines:
        parts = line.split()
        if "->" in parts:
            words.add(parts[0])
            index = parts.index("->")
            bad |= set([x.strip(",") for x in parts[index+1:]])
    for w in words:
        if w not in bad:
            return w


def circus_two(lines: list) -> int:
    bad = set()
    words = set()
    weights = {}
    children = defaultdict(list)

    for line in lines:
        parts = line.split()
        weights[parts[0]] = int(parts[1].strip("()"))
        if "->" in parts:
            index = parts.index("->")
            children[parts[0]] = set([x.strip(",") for x in parts[index + 1:]])
            words.add(parts[0])
            bad |= children[parts[0]]
    for w in words:
        if w not in bad:
            odd_ones = {}
            dfs(children, weights, w, 0, odd_ones)
            return odd_ones[max(odd_ones)]


def dfs(children: dict, weights: dict, root: str, depth: int, odd_ones: dict) -> int:
    expected = None
    s = weights[root]
    for child in children[root]:
        w = dfs(children, weights, child, depth+1, odd_ones)
        s += w
        if expected is None:
            expected = w
        elif expected != w:
            should = weights[child] + (expected - w)
            odd_ones[depth] = (child, should)
    return s


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

    print("One - Root Name:", circus_one(in_lines))
    print("Two - Unbalanced Node:", circus_two(in_lines))
