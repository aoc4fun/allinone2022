INPUT_FILE = "./input.txt"

test_strings = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", "bvwbjplbgvbhsrlpgdmjqwftvncz", "nppdvjthqldpwncqszvftbrmjlhg",
                "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
test_1_expected = [7, 5, 6, 10, 11]
test_2_expected = [19, 23, 23, 29, 26]


def test1():
    for i, test_string in enumerate(test_strings):
        assert part1(test_string) == test_1_expected[i]


def test2():
    for i, test_string in enumerate(test_strings):
        assert part2(test_string) == test_2_expected[i]


def detect_distinct_marker(line, marker_length):
    last_chars = ""
    for i, letter in enumerate(line):
        if letter in last_chars:
            last_chars = last_chars[last_chars.index(letter)+1:]
        last_chars += letter
        if len(last_chars) == marker_length:
            return i + 1
    return -1


# Could have been done by zipping the list 4 times with offsets
def part1(line):
    return detect_distinct_marker(line, 4)


def part2(line):
    return detect_distinct_marker(line, 14)


def main():
    test1()
    test2()

    with open(INPUT_FILE, "r") as file:
        print(part1(file.readline().strip()))
    with open(INPUT_FILE, "r") as file:
        print(part2(file.readline().strip()))


if __name__ == '__main__':
    main()
