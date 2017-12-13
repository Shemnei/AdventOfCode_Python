def firewall_one(layers: dict) -> int:
    severity = 0
    ticks = 0
    last_layer = 0
    for k, v in layers.items():
        ticks += (k - last_layer)
        last_layer = k
        iteration, scanner_layer_pos = divmod(ticks, v - 1)
        if iteration % 2 == 1:
            scanner_layer_pos = v - scanner_layer_pos
        if scanner_layer_pos == 0:
            severity += k * v

    return severity


def firewall_two(layers: dict) -> int:
    delay = 0

    while True:
        caught = False
        ticks = delay
        last_layer = 0
        for k, v in layers.items():
            ticks += (k - last_layer)
            last_layer = k
            iteration, scanner_layer_pos = divmod(ticks, v - 1)
            if iteration % 2 == 1:
                scanner_layer_pos = v - scanner_layer_pos
            if scanner_layer_pos == 0:
                caught = True
                break
        if not caught:
            break
        delay += 1

    return delay


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

    in_layers = {}
    for l in in_lines:
        parts = l.split(": ")
        in_layers[int(parts[0])] = int(parts[1])

    print("One - Firewall Severity:", firewall_one(in_layers))
    print("Two - Min Packet Delay:", firewall_two(in_layers))
