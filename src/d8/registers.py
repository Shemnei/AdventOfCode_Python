from collections import defaultdict


def registers_one(lines: list) -> (str, int):
    registers = defaultdict(lambda: 0)

    for line in lines:
        parts = line.split()
        register = parts[0]
        add_mod = -1 if parts[1] == "dec" else 1
        val = int(parts[2])
        parts[4] = f"registers[\"%s\"]" % parts[4]
        if eval(" ".join(parts[4:])):
            registers[register] += (add_mod * val)
    max_register = max(registers, key=registers.get)
    return max_register, registers[max_register]


def registers_two(lines: list) -> (str, int):
    registers = defaultdict(lambda: 0)
    max_value = None

    for line in lines:
        parts = line.split()
        register = parts[0]
        add_mod = -1 if parts[1] == "dec" else 1
        val = int(parts[2])
        parts[4] = f"registers[\"%s\"]" % parts[4]
        if eval(" ".join(parts[4:])):
            registers[register] += (add_mod * val)
            current_val = registers[register]
            if max_value is None or max_value[1] < current_val:
                max_value = (register, current_val)

    return max_value


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

    print("One - Max End Value:", registers_one(in_lines))
    print("Two - Max Overall Value:", registers_two(in_lines))
