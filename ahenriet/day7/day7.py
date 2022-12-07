class Directory(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.files = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_size(self):
        return sum(self.files) + sum([child.get_size() for child in self.children])

    def add_file(self, size):
        self.files.append(int(size))

    def get_path(self):
        if self.parent:
            return self.parent.get_path() + "/" + self.name
        else:
            return self.name

    def __repr__(self):
        return self.get_path()


def read_commands(efl_file):
    with open(efl_file, 'r') as f:
        commands = [line.replace("\n", "") for line in f.readlines()]
    return commands


class state(object):
    def __init__(self):
        self.root = Directory("")
        self.current = self.root


def parse_line(line, state):
    if line[0] == "$":
        command = line.split(" ")[1]
        if command == "cd":
            if line.split(" ")[2] == "/":
                return
            if line.split(" ")[2] == "..":
                state.current = state.current.parent
            else:
                new_dir = Directory(line.split(" ")[2])
                state.current.add_child(new_dir)
                state.current = new_dir
    else:
        if not "dir" in line.split(" ")[0]:
            state.current.add_file(line.split(" ")[0])


def parse_lines(lines, state):
    for line in lines:
        parse_line(line, state)
    return state


def filtered_list(directory, filter, result):
    if filter(directory.get_size()):
        result.append(directory)
    for child in directory.children:
        filtered_list(child, filter, result)
    return result


def part1(directory):
    return sum([x.get_size() for x in filtered_list(directory.root, lambda x: x < 100000, [])])


def part2(directory):
    free_space = 70000000 - directory.root.get_size()
    missing_space = 30000000 - free_space
    return min([x.get_size() for x in filtered_list(directory.root, lambda x: x > missing_space, [])])


def result(input):
    current_state = state()
    parse_lines(read_commands(input), current_state)
    while (current_state.current.parent != None):
        current_state.current = current_state.current.parent
    return (part1(current_state)), (part2(current_state))


def test():
    assert result("demo7.txt") == (95437, 24933642)


if __name__ == "__main__":
    test()
    part1, part2 = result("day7.txt")

    print(f"Result for part 1 is {part1}")
    print(f"Result for part 2 is {part2}")
