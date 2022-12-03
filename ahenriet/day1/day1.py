def find_richest(efl_file):
    with open(efl_file, 'r') as f: return max([sum([int(i) for i in x.split("\n")]) for x in "".join(f.readlines()).split("\n\n")])

def find_3_richest(efl_file):
    with open(efl_file, 'r') as f: return sum([sum([int(i) for i in x.split("\n")]) for x in "".join(f.readlines()).split("\n\n")][-3:])

assert(find_richest("demo1.txt")==24000)
print(find_richest("day1.txt"))

assert(find_3_richest("demo1.txt")==45000)
print(find_3_richest("day1.txt"))
