TEST_FILE = "./test.txt"
INPUT_FILE = "./input.txt"


def test1(file, expected):
    assert part1(file) == expected


def test2(file, expected):
    assert part2(file) == expected


def parse_file(file):
    current_dir = ""
    contents = dict()
    for line in file.readlines():
        line = line.strip()
        if line == "$ cd /":
            current_dir = ""
        elif line == "$ cd ..":
            current_dir = "/".join(current_dir.split("/")[0:-1])
        elif line.startswith("$ cd"):
            current_dir += "/" + line.split()[-1]
        elif line != "$ ls":
            current_dir_name = current_dir if current_dir != "" else "/"
            folder_content = contents.get(current_dir_name)
            if folder_content is None:
                folder_content = list()
            line_split = line.split()
            folder_content.append([int(line_split[0]) if line_split[0] != "dir" else -1, line_split[1]])
            contents[current_dir_name] = folder_content
    return contents


def compute_all_folders_sizes(contents):
    # Sort folders by depth to process the most in depth first and remove root
    folder_names = sorted(list(contents.keys()), key=lambda name: len(name.split("/")), reverse=True)
    folder_names.remove("/")

    folder_sizes = dict()

    for folder in folder_names:
        size = compute_folder_size(contents, folder, folder_sizes)
        folder_sizes[folder] = size

    folder_sizes["/"] = compute_folder_size(contents, "/", folder_sizes)

    return folder_sizes


# folder_sizes is expected to be defined for every subfolder
# This is the case as we sorted by depth
def compute_folder_size(contents, folder, folder_sizes):
    size = 0
    for file in contents.get(folder):
        if file[0] != -1:
            size += file[0]
        else:
            folder_name = folder + "/" + file[1] if folder != "/" else folder + file[1]
            size += folder_sizes.get(folder_name)
    return size


def part1(file):
    contents = parse_file(file)
    folder_sizes = compute_all_folders_sizes(contents)
    return sum(filter(lambda x: x < 100000, folder_sizes.values()))


def part2(file):
    contents = parse_file(file)
    folder_sizes = compute_all_folders_sizes(contents)
    required_space = 30000000 - (70000000 - folder_sizes.get("/"))
    return min(list(dict(filter(lambda x: x[1] > required_space, folder_sizes.items())).values()))


def main():
    with open(TEST_FILE, "r") as test_file:
        test1(test_file, 95437)
    with open(TEST_FILE, "r") as test_file:
        test2(test_file, 24933642)

    with open(INPUT_FILE, "r") as file:
        print(part1(file))
    with open(INPUT_FILE, "r") as file:
        print(part2(file))


if __name__ == '__main__':
    main()
