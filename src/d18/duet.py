from collections import defaultdict, deque


def duet_one(instructions: list) -> int:
    q0 = deque()

    for s in program(instructions, 0, q0, q0):
        if s == 'received':
            break
    return q0[-1]


def duet_two(instructions: list) -> int:
    q0 = deque()
    q1 = deque()
    send = 0
    p0 = program(instructions, 0, q0, q1)
    p1 = program(instructions, 1, q1, q0)

    while True:
        s_o = next(p0)
        s_t = next(p1)
        if s_t == "send":
            send += 1

        if s_o == s_t == "wait":
            return send


def program(instructions: list, pid: int, out_queue: deque, in_queue: deque):
    registers = defaultdict(lambda: 0)
    registers["p"] = pid
    pointer = 0
    while 0 <= pointer < len(instructions):
        i, x, y, *_ = (instructions[pointer] + " !").split(" ")
        x_v = int(x) if is_digit(x) else registers[x]
        y = int(y) if is_digit(y) else registers[y]
        if i == "snd":
            out_queue.append(x_v)
            yield "send"
        elif i == "set":
            registers[x] = y
        elif i == "add":
            registers[x] += y
        elif i == "mul":
            registers[x] *= y
        elif i == "mod":
            registers[x] %= y
        elif i == "rcv":
            while len(in_queue) == 0:
                yield "wait"
            else:
                registers[x] = in_queue.popleft()
                yield "received"
        elif i == "jgz":
            if x_v > 0:
                pointer += (y - 1)

        pointer += 1


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


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

    print("One - Recovered Value:", duet_one(in_lines))
    print("Two - Values Send:", duet_two(in_lines))
