import re
from operator import add


def swarm_one(particles: list) -> int:
    min_movement = ()
    for i in range(len(particles)):
        p, v, a = particles[i].split(", ")
        p = list(map(int, re.findall(r"(-?\d+)", p)))
        v = list(map(int, re.findall(r"(-?\d+)", v)))
        a = list(map(int, re.findall(r"(-?\d+)", a)))

        acc = sum(map(abs, a))
        vel = sum(map(abs, v))
        vel_1 = sum(map(abs, tuple(map(add, v, a))))
        if vel_1 < vel:
            vel = -vel
        movement = (i, acc, vel)

        if not min_movement:
            min_movement = movement
        elif min_movement[1] > movement[1]:
            min_movement = movement
        elif min_movement[1] == movement[1]:
            if min_movement[2] > movement[2]:
                min_movement = movement

    return min_movement[0]


def swarm_two(in_particles: list) -> int:
    particles = []
    for i in range(len(in_particles)):
        p, v, a = in_particles[i].split(", ")
        p = tuple(map(int, re.findall(r"(-?\d+)", p)))
        v = tuple(map(int, re.findall(r"(-?\d+)", v)))
        a = tuple(map(int, re.findall(r"(-?\d+)", a)))
        particles.append([p, v, a])

    ticks = 1_000
    for t in range(ticks):
        for i in range(len(particles)):
            v = particles[i]
            new_vel = tuple(sum(t) for t in zip(v[1], v[2]))
            new_pos = list(sum(t) for t in zip(v[0], new_vel))
            particles[i] = [new_pos, new_vel, v[2]]
        positions = [x[0] for x in particles]
        collisions = [i for i, x in enumerate(positions) if positions.count(x) > 1]
        [particles.pop(i) for i in collisions[::-1]]

    return len(particles)


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

    print("One - Closest to <0,0,0>:", swarm_one(in_lines))
    print("Two - Particles remaining:", swarm_two(in_lines))
