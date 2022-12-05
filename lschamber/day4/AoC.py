TEST_FILE = "./test.txt"
INPUT_FILE = "./input.txt"


def test1(file, expected):
    assert part1(file) == expected


def test2(file, expected):
    assert part2(file) == expected


def is_overlapping(line):
    elf1, elf2 = line
    return any(elem in elf1 for elem in elf2)


def is_fully_overlapping(line):
    elf1, elf2 = line
    if len(elf1) < len(elf2):
        elf1, elf2 = elf2, elf1
    return all(elem in elf1 for elem in elf2)


def part1(file):
    elves_ranges = [[list(range(int(elf.split('-')[0]), int(elf.split('-')[1]) + 1)) for elf in line.strip().split(",")]
                    for line in file.readlines()]
    nb_overlapping = sum(list(map(is_fully_overlapping, elves_ranges)))
    return nb_overlapping


def part2(file):
    return sum([any(
        elem in range(int(line.strip().split(",")[0].split('-')[0]), int(line.strip().split(",")[0].split('-')[1]) + 1)
        for elem in
        range(int(line.strip().split(",")[1].split('-')[0]), int(line.strip().split(",")[1].split('-')[1]) + 1)) for
                line in file.readlines()])


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, 2)
    with open(TEST_FILE, "r") as test_file:
        test2(test_file, 4)

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
    with open(INPUT_FILE, "r") as file:
        print(part2(file))


if __name__ == '__main__':
    main()
