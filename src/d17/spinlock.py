def spinlock_one(steps: int) -> int:
    buffer = [0]
    cur_pos = 0
    iterations = 2017

    for iter in range(1, iterations+1):
        cur_pos += steps
        cur_pos %= len(buffer)
        cur_pos += 1
        buffer.insert(cur_pos, iter)

    return buffer[(buffer.index(2017) + 1) % len(buffer)]


def spinlock_two(steps: int) -> int:
    cur_pos = 0
    iterations = 50_000_000
    val_after_0 = 0

    for i in range(1, iterations + 1):
        cur_pos = (cur_pos + steps) % i + 1
        if cur_pos == 1:
            val_after_0 = i

    return val_after_0


if __name__ == '__main__':
    value = input()

    if not value:
        with open("input.txt", "r") as f:
            value = f.read()
    value = int(value)

    print("One - Value after 2017:", spinlock_one(value))
    print("Two - Value after 0:", spinlock_two(value))
