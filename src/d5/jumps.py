def jump_one(jumps: list) -> int:
    step_count = 0
    current_index = 0
    work_list = list(jumps)
    while current_index < len(work_list):
        offset = work_list[current_index]
        work_list[current_index] += 1
        current_index += offset
        step_count += 1
    return step_count


def jump_two(jumps: list) -> int:
    step_count = 0
    current_index = 0
    work_list = list(jumps)
    while current_index < len(work_list):
        offset = work_list[current_index]
        work_list[current_index] += -1 if offset >= 3 else 1
        current_index += offset
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

    print("Jumps One:", jump_one(in_lines))
    print("Jumps Two:", jump_two(in_lines))
