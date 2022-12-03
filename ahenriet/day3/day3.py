
def intersect_method_1(games):
    return [set(game[:round((len(game))/2)]).intersection(set(game[round((len(game)) / 2):])).pop() for game in games]

def intersect_method_2(games):
    return [set(games[0 + i]).intersection(set(games[1 + i])).intersection(games[2 + i]).pop()
                  for i in range(0, len(games), 3)]

def priorities_compute(efl_file,intersect_method=intersect_method_1):
    with open(efl_file, 'r') as f:
        games=[x.replace("\n","") for x in f.readlines()]
        return sum([ord(intersect)-ord("&") if intersect<"a" else ord(intersect)-ord("`") for intersect in intersect_method(games)])

print(priorities_compute("demo3.txt"))
print(priorities_compute("day3.txt"))

print(priorities_compute("demo3.txt",intersect_method=intersect_method_2))
print(priorities_compute("day3.txt",intersect_method=intersect_method_2))