TEST_FILE = "./test.txt"
INPUT_FILE = "./input.txt"


def test1(file, expected):
    assert part1(file) == expected


def test2(file, expected):
    assert part2(file) == expected


def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))


def compute_priority_map():
    prio_map = dict()
    for char_val in range(ord('a'), ord('z') + 1):
        prio_map[chr(char_val)] = char_val - 96
    for char_val in range(ord('A'), ord('Z') + 1):
        prio_map[chr(char_val)] = char_val - 38
    return prio_map


def split_middle(l):
    middle = int(len(l) / 2)
    return [l[:middle], l[middle:]]


def part1(file):
    prio_map = compute_priority_map()
    return sum([prio_map[(set(bag[0]).intersection(bag[1])).pop()]
                for bag in [split_middle([char for char in line.strip()])
                            for line in file.readlines()]])


def part2(file):
    prio_map = compute_priority_map()
    return sum([prio_map[(set(group[0]).intersection(group[1]).intersection(group[2])).pop()]
                for group in zip(*([iter([[char for char in line.strip()]
                                          for line in file.readlines()])] * 3))])


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, 157)
    with open(TEST_FILE, "r") as test_file:
        test2(test_file, 70)

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
    with open(INPUT_FILE, "r") as file:
        print(part2(file))


if __name__ == '__main__':
    main()
