TEST_FILE = "./test.txt"
INPUT_FILE = "./input"


def test1(file, expected):
    assert part1(file) == expected


def test2(file, expected):
    assert part2(file) == expected


def compute_signal(file):
    current_cycle = 0
    X = 1
    signal = 0
    for line in file.readlines():
        line = line.split()
        current_cycle += 1

        if current_cycle == 20 or (current_cycle + 20) % 40 == 0:
            # print(current_cycle, line, X)
            signal += current_cycle * X
        if len(line) > 1:
            current_cycle += 1
            if current_cycle == 20 or (current_cycle + 20) % 40 == 0:
                # print(current_cycle, line, X, 'Part 2')
                signal += current_cycle * X
            X += int(line[1])

    return signal


def part1(file):
    return compute_signal(file)


def part2(file):
    X = 1
    current_line = ""
    for line in file.readlines():
        line = line.split()
        if X - 1 <= len(current_line) <= X + 1:
            current_line += "#"
        else:
            current_line += "."
        if len(current_line) == 40:
            print(current_line)
            current_line = ""

        if len(line) > 1:
            if X - 1 <= len(current_line) <= X + 1:
                current_line += "#"
            else:
                current_line += "."
            if len(current_line) == 40:
                print(current_line)
                current_line = ""
            X += int(line[1])


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, 13140)
    with open(TEST_FILE, "r") as test_file:
        part2(test_file)

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
    with open(INPUT_FILE, "r") as file:
        part2(file)


if __name__ == '__main__':
    main()
