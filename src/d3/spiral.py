import math


def spiral_one(val: int) -> int:
    layer = math.ceil(math.sqrt(val))
    layer = layer + 1 if layer % 2 == 0 else layer
    to_center = int(layer/2)

    min_val = ((layer - 1)**2) + 1
    max_val = layer**2

    bottom_right = max_val
    bottom_left = bottom_right - (layer - 1)
    top_left = bottom_left - (layer - 1)
    top_right = top_left - (layer - 1)

    print("layer: ", layer)
    print("min: ", min_val)
    print("max: ", max_val)
    print("diff: ", max_val - min_val)

    print("top_left_corner: ", top_left)
    print("top_right_corner: ", top_right)
    print("bottom_right_corner: ", bottom_right)
    print("bottom_left_corner: ", bottom_left)

    if value <= top_right:
        middle = top_right - int(layer/2)
        print("value -> right")
        return int(to_center + math.fabs(val - middle))
    if value <= top_left:
        middle = top_right + int(layer/2)
        print("value -> top")
        return int(to_center + math.fabs(val - middle))
    if value <= bottom_left:
        middle = bottom_left - int(layer/2)
        print("value -> left")
        return int(to_center + math.fabs(val - middle))
    middle = bottom_left + int(layer / 2)
    print("value -> bottom")
    return int(to_center + math.fabs(val - middle))


def spiral_two(val: int) -> int:
    # matrix middle
    m = int(math.ceil(math.sqrt(val)) / 2)
    # matrix size
    h = 2 * m - 1
    # matrix
    a = [[0 for x in range(h)] for y in range(h)]
    # set start
    a[m][m] = 1
    # offsets
    t = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]

    for i in range(2, m**2):
        layer = math.ceil(math.sqrt(i))
        layer = layer + 1 if layer % 2 == 0 else layer
        to_center = int(layer / 2)
        max_val = layer ** 2
        bottom_right = max_val
        bottom_left = bottom_right - (layer - 1)
        top_left = bottom_left - (layer - 1)
        top_right = top_left - (layer - 1)
        if i <= top_right:  # right
            middle = top_right - int(layer / 2)
            x, y = [m + to_center, m - (i - middle)]
        elif i <= top_left: # top
            middle = top_right + int(layer / 2)
            x, y = [m - (i - middle), m - to_center]
        elif i <= bottom_left:  # left
            middle = bottom_left - int(layer / 2)
            x, y = [m - to_center, m + (i - middle)]
        else:   # bottom
            middle = bottom_left + int(layer / 2)
            x, y = [m + (i - middle), m + to_center]

        v_sum = 0
        for (xo, yo) in t:
            nx, ny = [(x + xo), (y + yo)]
            if nx > h or ny > h:
                continue
            v_sum += a[nx][ny]
        print("Index %d, (%d, %d) => %d" % (i, x, y, v_sum))
        if v_sum > val:
            return v_sum
        a[x][y] = v_sum


if __name__ == '__main__':
    value = input()
    if not value or isinstance(value, int):
        with open("input.txt", "r") as f:
            value = int(f.read())

    print("Spiral One (Steps):", spiral_one(value))
    print("-"*10)
    print("Spiral Two (Value):", spiral_two(value))
