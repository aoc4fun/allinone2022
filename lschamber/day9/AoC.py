TEST_FILE = "./test.txt"
TEST_FILE_2 = "./test2.txt"
INPUT_FILE = "./input"


def test1(file, expected):
    assert part1(file) == expected


def test2(file, expected):
    assert part2(file) == expected


def parse_file(file):
    return [(line.strip().split()[0], int(line.strip().split()[1])) for line in file.readlines()]


def move_h(h, direction):
    if direction == 'R':
        h[0] += 1
    elif direction == 'L':
        h[0] -= 1
    elif direction == 'U':
        h[1] += 1
    elif direction == 'D':
        h[1] -= 1
    return h


def move_t(h, t):
    distance_x = t[0] - h[0]
    distance_y = t[1] - h[1]

    # If moved in diag
    if abs(distance_x) + abs(distance_y) >= 3:
        if distance_y == -2:
            t = [h[0], h[1] - 1]
        elif distance_x == -2:
            t = [h[0] - 1, h[1]]
        elif distance_y == 2:
            t = [h[0], h[1] + 1]
        elif distance_x == 2:
            t = [h[0] + 1, h[1]]
    else:
        if distance_y <= -2:
            t[1] = h[1] - 1
        elif distance_y >= 2:
            t[1] = h[1] + 1

        if distance_x <= -2:
            t[0] = h[0] - 1
        elif distance_x >= 2:
            t[0] = h[0] + 1

    return t


def part1(file):
    moves = parse_file(file)
    t_positions = set()
    h = [0, 0]
    t = [0, 0]
    for move in moves:
        for _ in range(move[1]):
            h = move_h(h, move[0])
            t = move_t(h, t)
            t_positions.add((t[0], t[1]))
    return len(t_positions)


def part2(file):
    moves = parse_file(file)
    t_positions = set()
    h = [0, 0]
    t_1 = [0, 0]
    t_2 = [0, 0]
    t_3 = [0, 0]
    t_4 = [0, 0]
    t_5 = [0, 0]
    t_6 = [0, 0]
    t_7 = [0, 0]
    t_8 = [0, 0]
    t_9 = [0, 0]

    for move in moves:
        for _ in range(move[1]):
            h = move_h(h, move[0])
            t_1 = move_t(h, t_1)
            t_2 = move_t(t_1, t_2)
            t_3 = move_t(t_2, t_3)
            t_4 = move_t(t_3, t_4)
            t_5 = move_t(t_4, t_5)
            t_6 = move_t(t_5, t_6)
            t_7 = move_t(t_6, t_7)
            t_8 = move_t(t_7, t_8)
            t_9 = move_t(t_8, t_9)
            t_positions.add((t_9[0], t_9[1]))
    return len(t_positions)


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, 13)
    with open(TEST_FILE, "r") as test_file:
        test2(test_file, 1)
    with open(TEST_FILE_2, "r") as test_file:
        test2(test_file, 36)

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
    with open(INPUT_FILE, "r") as file:
        print(part2(file)) #Not Working


if __name__ == '__main__':
    main()
