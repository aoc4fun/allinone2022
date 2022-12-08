TEST_FILE = "./test.txt"
INPUT_FILE = "./input"


def test1(file, expected):
    assert part1(file) == expected


def test1_2(file):
    trees = compute_map(file)

    assert visible_from_left(trees, 1, 1)
    assert visible_from_top(trees, 1, 1)
    assert not visible_from_right(trees, 1, 1)
    assert not visible_from_bot(trees, 1, 1)
    assert visible(trees, 1, 1)

    assert not visible_from_left(trees, 2, 1)
    assert visible_from_top(trees, 2, 1)
    assert visible_from_right(trees, 2, 1)
    assert not visible_from_bot(trees, 2, 1)
    assert visible(trees, 2, 1)

    assert not visible(trees, 3, 1)

    assert not visible_from_left(trees, 1, 2)
    assert not visible_from_top(trees, 1, 2)
    assert visible_from_right(trees, 1, 2)
    assert not visible_from_bot(trees, 1, 2)
    assert visible(trees, 1, 2)

    assert not visible_from_left(trees, 2, 2)
    assert not visible_from_top(trees, 2, 2)
    assert not visible_from_right(trees, 2, 2)
    assert not visible_from_bot(trees, 2, 2)
    assert not visible(trees, 2, 2)

    assert not visible_from_left(trees, 3, 2)
    assert not visible_from_top(trees, 3, 2)
    assert visible_from_right(trees, 3, 2)
    assert not visible_from_bot(trees, 3, 2)
    assert visible(trees, 3, 2)

    assert not visible_from_left(trees, 1, 3)
    assert not visible_from_top(trees, 1, 3)
    assert not visible_from_right(trees, 1, 3)
    assert not visible_from_bot(trees, 1, 3)
    assert not visible(trees, 1, 3)

    assert visible_from_left(trees, 2, 3)
    assert not visible_from_top(trees, 2, 3)
    assert not visible_from_right(trees, 2, 3)
    assert visible_from_bot(trees, 2, 3)
    assert visible(trees, 2, 3)

    assert not visible_from_left(trees, 3, 3)
    assert not visible_from_top(trees, 3, 3)
    assert not visible_from_right(trees, 3, 3)
    assert not visible_from_bot(trees, 3, 3)
    assert not visible(trees, 3, 3)


def test2(file, expected):
    assert part2(file) == expected


def trees_on_left(tree_map, x, y):
    return tree_map[y][:x]


def visible_from_left(tree_map, x, y):
    return all(tree < tree_map[y][x] for tree in trees_on_left(tree_map, x, y))


def trees_on_right(tree_map, x, y):
    return tree_map[y][x + 1:]


def visible_from_right(tree_map, x, y):
    return all(tree < tree_map[y][x] for tree in trees_on_right(tree_map, x, y))


def trees_on_top(tree_map, x, y):
    return list(map(lambda line: line[x], tree_map[:y]))


def visible_from_top(tree_map, x, y):
    return all(tree < tree_map[y][x] for tree in trees_on_top(tree_map, x, y))


def trees_on_bot(tree_map, x, y):
    return list(map(lambda line: line[x], tree_map[y + 1:]))


def visible_from_bot(tree_map, x, y):
    return all(tree < tree_map[y][x] for tree in trees_on_bot(tree_map, x, y))


def visible(tree_map, x, y):
    return visible_from_left(tree_map, x, y) or visible_from_right(tree_map, x, y) or visible_from_bot(tree_map, x, y) \
           or visible_from_top(tree_map, x, y)


def compute_map(file):
    return [[int(x) for x in line.strip()] for line in file.readlines()]


def part1(file):
    tree_map = compute_map(file)
    nb_tree_visible = len(tree_map) * 2 + len(tree_map[0]) * 2 - 4  # All outermost trees
    for y in range(1, len(tree_map) - 1):
        for x in range(1, len(tree_map[0]) - 1):
            if visible(tree_map, x, y):
                nb_tree_visible += 1

    return nb_tree_visible


def scenery_on_right(tree_map, x, y):
    return number_of_visible_trees(trees_on_right(tree_map, x, y), tree_map[y][x])


def scenery_on_left(tree_map, x, y):
    return number_of_visible_trees(reversed(trees_on_left(tree_map, x, y)), tree_map[y][x])


def scenery_on_bot(tree_map, x, y):
    return number_of_visible_trees(trees_on_bot(tree_map, x, y), tree_map[y][x])


def scenery_on_top(tree_map, x, y):
    return number_of_visible_trees(reversed(trees_on_top(tree_map, x, y)), tree_map[y][x])


# ****** The Elves don't care about distant trees taller than those found by the rules above; ******* Did not understood it
def number_of_visible_trees(tree_list, inital):
    direction_score = 0
    for current_tree in tree_list:
        if current_tree >= inital:
            return direction_score + 1
        direction_score += 1
    return direction_score


def score_for_a_position(tree_map, x, y):
    r = scenery_on_right(tree_map, x, y)
    l = scenery_on_left(tree_map, x, y)
    t = scenery_on_top(tree_map, x, y)
    b = scenery_on_bot(tree_map, x, y)
    total = r * l * t * b
    return total


def part2(file):
    scores = list()
    tree_map = compute_map(file)
    score_map = ""
    for y in range(1, len(tree_map) - 1):
        for x in range(1, len(tree_map[0]) - 1):
            scores.append(score_for_a_position(tree_map, x, y))
            score_map += str(score_for_a_position(tree_map, x, y)) + ","
        score_map += "\n"
    return max(scores)


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, 21)
    with open(TEST_FILE, "r") as test_file:
        test1_2(test_file)
    with open(TEST_FILE, "r") as test_file:
        test2(test_file, 8)

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
    with open(INPUT_FILE, "r") as file:
        print(part2(file))


if __name__ == '__main__':
    main()
