def captcha_sum_one(captcha: str) -> int:
    c_sum = 0
    length = len(captcha)
    for i, c1 in enumerate(captcha):
        c2 = captcha[(i + 1) % length]
        if c1 == c2:
            c_sum += int(c1)
    return c_sum


def captcha_sum_two(captcha: str) -> int:
    length = len(captcha)
    offset = int(length / 2)
    part_one = captcha[:offset]
    part_two = captcha[offset:]
    c_sum = 0
    for c1, c2 in zip(part_one, part_two):
        if c1 == c2:
            c_sum += int(c1)*2
    return c_sum


if __name__ == '__main__':
    value = input()
    print(captcha_sum_one(value))
    print(captcha_sum_two(value))
