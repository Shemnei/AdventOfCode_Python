def jump_one(jumps: list) -> int:
    step_count = 0
    current_index = 0
    offset_dict = {key: 0 for key in range(0, len(jumps))}

    while current_index < len(jumps):
        offset = jumps[current_index] + offset_dict[current_index]
        offset_dict[current_index] += 1
        current_index = current_index + offset
        step_count += 1
    return step_count


def jump_two(jumps: list) -> int:
    step_count = 0
    current_index = 0
    offset_dict = {key: 0 for key in range(0, len(jumps))}

    while current_index < len(jumps):
        offset_add_amount = offset_dict[current_index]
        offset = jumps[current_index] + offset_add_amount
        if offset >= 3:
            offset_dict[current_index] -= 1
        else:
            offset_dict[current_index] += 1
        current_index = current_index + offset
        step_count += 1
    return step_count


if __name__ == '__main__':
    in_lines = []
    while True:
        line = input()
        if line:
            in_lines.append(line)
        else:
            break

    if not in_lines:
        with open("input.txt", "r") as f:
            in_lines = f.read().splitlines()
    in_lines = [int(x) for x in in_lines]

    print("Jumps One: ", jump_one(in_lines))
    print("Jumps Two: ", jump_two(in_lines))
