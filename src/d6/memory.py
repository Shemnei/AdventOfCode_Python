def memory_one(values: list) -> int:
    memory_memory = set()
    memory_state = list(values)
    while tuple(memory_state) not in memory_memory:
        memory_memory.add(tuple(memory_state))
        v = max(memory_state)
        i = memory_state.index(v)
        memory_state[i] = 0
        for _ in range(v):
            i = (i + 1) % len(memory_state)
            memory_state[i] += 1
    return len(memory_memory)


def memory_two(values: list) -> int:
    memory_memory = {}
    memory_state = list(values)
    memory_state_tuple = tuple(memory_state)
    while memory_state_tuple not in memory_memory:
        memory_memory[memory_state_tuple] = len(memory_memory)
        v = max(memory_state)
        i = memory_state.index(v)
        memory_state[i] = 0
        for _ in range(v):
            i = (i + 1) % len(memory_state)
            memory_state[i] += 1
        memory_state_tuple = tuple(memory_state)
    return len(memory_memory) - memory_memory[memory_state_tuple]


if __name__ == '__main__':
    value = input()

    if not value:
        with open("input.txt", "r") as f:
            value = f.read()
    value = [int(x) for x in value.split()]

    print("One - Loop after: ", memory_one(value))
    print("Two - Loop after: ", memory_two(value)) #2765
