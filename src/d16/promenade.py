def promenade_one(steps: list) -> str:
    order = [chr(ord("a") + x) for x in range(16)]
    for step in steps:
        if step[0] == "s":
            index = int(step[1:])
            order = order[-index:] + order[:-index]
        elif step[0] == "x":
            index_one, index_two = [int(x) for x in step[1:].split("/")]
            order[index_one], order[index_two] = order[index_two], order[index_one]
        elif step[0] == "p":
            index_one = order.index(step[1])
            index_two = order.index(step[3])
            order[index_one], order[index_two] = order[index_two], order[index_one]
    return "".join(order)


def promenade_two(steps: list) -> str:
    order = [chr(ord("a") + x) for x in range(16)]

    seen = []
    iterations = 1_000_000_000
    for i in range(iterations):
        str_rep = "".join(order)
        if str_rep in seen:
            print(i)
            return seen[iterations % i]
        seen.append(str_rep)

        for step in steps:
            if step[0] == "s":
                index = int(step[1:])
                order = order[-index:] + order[:-index]
            elif step[0] == "x":
                index_one, index_two = [int(x) for x in step[1:].split("/")]
                order[index_one], order[index_two] = order[index_two], order[index_one]
            elif step[0] == "p":
                index_one = order.index(step[1])
                index_two = order.index(step[3])
                order[index_one], order[index_two] = order[index_two], order[index_one]
    return "".join(order)


if __name__ == '__main__':
    value = input()

    if not value:
        with open("input.txt", "r") as f:
            value = f.read()

    values = value.split(",")

    print("One - New Order:", promenade_one(values))
    print("Two - New Order:", promenade_two(values))
