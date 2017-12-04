def checksum_one(val: list) -> int:
    c_sum = 0
    for l in val:
        parts = [int(x) for x in l.split()]
        parts.sort()
        print(parts)
        c_sum += (int(parts[-1]) - int(parts[0]))
    return c_sum


def checksum_two(val: list) -> int:
    c_sum = 0
    for l in val:
        parts = [int(x) for x in l.split()]
        for i, n in enumerate(parts):
            for ii in range(i + 1, len(parts)):
                div_result_one = n / parts[ii]
                div_result_two = parts[ii] / n
                if div_result_one == int(div_result_one):
                    c_sum += div_result_one
                    break
                elif div_result_two == int(div_result_two):
                    c_sum += div_result_two
                    break
    return int(c_sum)


if __name__ == '__main__':
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    print(checksum_one(lines))
    print(checksum_two(lines))
