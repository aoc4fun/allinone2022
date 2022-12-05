TEST_FILE = "./test.txt"
INPUT_FILE = "./input.txt"



def part1(data):
    sizes = compute_elves_inventory(data)
    print(max(sizes))


def part2(data):
    sizes = compute_elves_inventory(data)
    top_three = sum(sorted(sizes, reverse=True)[:3])
    print(top_three)
    return None

def compute_elves_inventory(data):
    return [sum(x) for x in data]

def parse_file(file):
    all_elves = []
    current_elf = []
    for x in file.readlines():
        if x == '\n':
            all_elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(x))
    all_elves.append(current_elf)
    return all_elves



def test1(file, expected):
    assert part1(file) == expected


def test2(file, expected):
    assert part2(file) == expected


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, None)
        test2(test_file, None)

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
        print(part2(file))


if __name__ == '__main__':
    main()

