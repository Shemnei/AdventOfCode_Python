def draw_img(img: list):
    for row in img:
        print("".join(row))


def str_rep(img: list) -> str:
    rep = ""
    for row in img:
        rep += "".join(row)
    return rep


def get_square(img: list, x: int, y: int, sqr_size: int) -> list:
    sqr_img = []
    x_pos = x * sqr_size
    y_pos = y * sqr_size
    for x in range(sqr_size):
        sqr_img.append(img[y_pos + x][x_pos:x_pos + sqr_size])
    return sqr_img


def insert_square(img: list, x: int, y: int, sqr_img: list):
    sqr_size = len(sqr_img)
    x_pos = x * sqr_size
    y_pos = y * sqr_size
    for x in range(sqr_size):
        img[y_pos + x][x_pos:x_pos + sqr_size] = sqr_img[x]


def rotate_square(img: list) -> list:
    size = len(img)
    r_img = []
    for x in range(size):
        row = []
        for y in range(size):
            row += img[::-1][y][::-1][(size - x - 1)]
        r_img.append(row)
    return r_img


def hflip_square(img: list) -> list:
    return img[::-1]


def vflip_square(img: list) -> list:
    return [row[::-1] for row in img]


def art_one(in_rules: list, iterations: int = 5) -> int:
    image = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]

    # parse rules
    rules2 = {}
    rules3 = {}
    for r in in_rules:
        inp, out = [x.strip() for x in r.split(" => ")]
        inp = [list(row) for row in inp.split("/")]
        out = [list(row) for row in out.split("/")]
        if len(inp) % 2 == 0:
            for i in range(4):
                inp = rotate_square(inp)
                rules2[str_rep(inp)] = out
                inp = vflip_square(inp)
                rules2[str_rep(inp)] = out
                inp = hflip_square(inp)
                rules2[str_rep(inp)] = out
        else:
            for i in range(4):
                inp = rotate_square(inp)
                rules3[str_rep(inp)] = out
                inp = vflip_square(inp)
                rules3[str_rep(inp)] = out
                inp = hflip_square(inp)
                rules3[str_rep(inp)] = out

    for i in range(iterations):
        size = len(image)
        if size % 2 == 0:
            squares = int(size / 2)
            rules = rules2
            sqr_size = 2
        else:
            squares = int(size / 3)
            rules = rules3
            sqr_size = 3

        new_size = (sqr_size + 1) * squares
        new_img = [list("." * new_size) for i in range(new_size)]

        for s in range(squares * squares):
            x = s % squares
            y = int(s / squares)
            sqr_img = get_square(image, x, y, sqr_size)
            str_rep_img = str_rep(sqr_img)
            if str_rep_img in rules:
                out_img = rules[str_rep_img]
                insert_square(new_img, x, y, out_img)
            else:
                print("NONE FOUND FOR (%d, %d)" % (x, y))
                draw_img(sqr_img)
                exit(1)
        image = new_img
    return sum([x.count("#") for x in image])


def art_two(rules: list) -> int:
    return art_one(rules, 18)


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

    print("One - 'On' Cells after 5iter:", art_one(in_lines))
    print("Two - 'On' Cells after 18iter:", art_two(in_lines))
