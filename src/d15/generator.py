def generator(value: int, factor: int, criteria: int = None):
    while True:
        value *= factor
        value %= 2147483647
        if criteria:
            if value % criteria == 0:
                yield value
        else:
            yield value


def bin_equals(val_a: int, val_b: int) -> bool:
    return bin(val_a)[2:][-16:] == bin(val_b)[2:][-16:]


def generator_one(gen: tuple) -> int:
    gen_a = generator(gen[0], 16807)
    gen_b = generator(gen[1], 48271)
    matches = 0

    for i in range(40_000_000):
        val_a = next(gen_a)
        val_b = next(gen_b)
        if bin_equals(val_a, val_b):
            matches += 1
    return matches


def generator_two(gen: tuple) -> int:
    gen_a = generator(gen[0], 16807, 4)
    gen_b = generator(gen[1], 48271, 8)
    matches = 0

    for i in range(5_000_000):
        val_a = next(gen_a)
        val_b = next(gen_b)
        if bin_equals(val_a, val_b):
            matches += 1
    return matches


if __name__ == '__main__':
    generators = (289, 629)
    print("One - Matches:", generator_one(generators))
    print("Two - Matches:", generator_two(generators))
