def plumber_one(programs: dict) -> int:
    program_set = set()
    program_stack = []

    program_stack += programs[0]
    while len(program_stack) > 0:
        v = program_stack.pop(0)
        if v in program_set:
            continue
        program_stack += programs[v]
        program_set.add(v)
    return len(program_set)


def plumber_two(programs: dict) -> int:
    groups = 0
    program_set = set()
    program_stack = []

    while len(programs) > 0:
        program_stack += next(iter(programs.values()))
        while len(program_stack) > 0:
            v = program_stack.pop(0)
            if v in program_set:
                continue
            program_stack += programs[v]
            program_set.add(v)
        for ps in program_set:
            programs.pop(ps)
        program_set.clear()
        program_stack.clear()
        groups += 1

    return groups


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

    progs = {}
    for l in in_lines:
        parts = l.split(" <-> ")
        progs[int(parts[0])] = [int(x.strip()) for x in parts[1].split(",")]

    print("One - Program Count:", plumber_one(progs))
    print("Two - Group Count:", plumber_two(progs))
