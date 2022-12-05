
TEST_FILE = "./test.txt"
INPUT_FILE = "./input.txt"


def test1(file, expected):
    assert part1(file) == expected


def test2(file, expected):
    assert part2(file) == expected


def parse_file(file):
    file_content =  [line for line in file.readlines()]
    stacks_lines = list()
    moves_lines = list()
    number_of_stack = None
    for i, line in enumerate(file_content):
        if line == '\n':
            stacks_lines = file_content[0:i-1]
            moves_lines = list(map(lambda x: [int(x[1]), int(x[3]), int(x[5])], [move.split() for move in file_content[i+1:]]))
            number_of_stack = int(file_content[i-1].strip()[-1])
    stacks = [""] * number_of_stack
    for line in reversed(stacks_lines):
        current_start = 0
        first_elt = line.find('[', current_start)
        while first_elt != -1 :
            stack = int(first_elt/4)
            stacks[stack] += line[first_elt+1]
            current_start = first_elt + 1
            first_elt = line.find('[', current_start)
    stacks = [list(stack) for stack in stacks]
    return stacks, moves_lines


def part1(file):
    (stacks, moves) = parse_file(file)

    for move in moves:
        for i in range(move[0]):
            stacks[move[2]-1] += stacks[move[1]-1].pop()

    return "".join(list(map(lambda stack: stack[-1], stacks)))


def part2(file):
    (stacks, moves) = parse_file(file)

    for move in moves:
        stacks[move[2]-1] += stacks[move[1]-1][-move[0]:]
        stacks[move[1]-1] = stacks[move[1]-1][:-move[0]]

    return "".join(list(map(lambda stack: stack[-1], stacks)))


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, "CMZ")
    with open(TEST_FILE, "r") as test_file:
        test2(test_file, "MCD")

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
    with open(INPUT_FILE, "r") as file:
        print(part2(file))


if __name__ == '__main__':
    main()
