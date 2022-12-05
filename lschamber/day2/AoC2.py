TEST_FILE = "./test.txt"
INPUT_FILE = "./input.txt"


def test1(file, expected):
    assert part1(file) == expected


def test2(file, expected):
    assert part2(file) == expected


def part1(file):
    scores = [compute_round_score_1(round) for round in parse_file(file)]
    return sum(scores)


def parse_file(file):
    return [[y for y in x.split()] for x in file.readlines()]


def compute_round_score_1(line):
    score_dict = {'X': 1, 'Y': 2, 'Z': 3}
    VICTORY = 6
    DRAW = 3

    score = score_dict.get(line[1])

    if is_draw(line):
        score += DRAW
    elif is_win(line):
        score += VICTORY

    return score


def compute_round_score_2(line):
    score_dict = {'A': 1, 'B': 2, 'C': 3}
    VICTORY = 6
    DRAW = 3

    player_line = [line[0], compute_expected_play(line)]
    score = score_dict.get(player_line[1])

    if line[1] == 'Y':
        score += DRAW
    elif line[1] == 'Z':
        score += VICTORY

    return score


def compute_expected_play(line):
    win_dict = {'A': 'B', 'B': 'C', 'C': 'A'}
    lose_dict = {'A': 'C', 'B': 'A', 'C': 'B'}

    if line[1] == 'Y':
        return line[0]
    elif line[1] == 'Z':
        return win_dict.get(line[0])
    else:
        return lose_dict.get(line[0])


def is_draw(line):
    return line[0] == 'A' and line[1] == 'X' or line[0] == 'B' and line[1] == 'Y' or line[0] == 'C' and line[1] == 'Z'


def is_win(line):
    return line[0] == 'A' and line[1] == 'Y' or line[0] == 'B' and line[1] == 'Z' or line[0] == 'C' and line[1] == 'X'


def part2(file):
    vals = [compute_round_score_2(round) for round in parse_file(file)]
    return sum(vals)


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, 15)
    with open(TEST_FILE, "r") as test_file:
        test2(test_file, 12)

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
    with open(INPUT_FILE, "r") as file:
        print(part2(file))


if __name__ == '__main__':
    main()
