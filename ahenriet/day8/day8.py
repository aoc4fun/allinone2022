import numpy as np

def read_map(efl_file):
    with open(efl_file, 'r') as f:
        map = [list(line.replace("\n", "")) for line in f.readlines()]
    return map

def is_visible(map,i,j):
    height=map[i][j]
    global_visibility=[]
    if max(map.T[j][0:i])>=height:
        global_visibility.append("N")
    if max(map.T[j][i+1:len(map)])>=height:
        global_visibility.append("S")

    if max(map[i][0:j])>=height:
        global_visibility.append("E")
    if max(map[i][j+1:len(map[0])])>=height:
        global_visibility.append("O")
    return len(set(global_visibility))<4

import math

def scenic_score(map,i,j):
    height=map[i][j]
    score=0
    scenic_arount=[]
    for k in range(i-1,-1,-1):
        score += 1
        if map[k][j]>=height:
             break
    scenic_arount.append(score)
    score = 0
    for k in range(i+1,len(map)):
        score += 1
        if map[k][j]>=height:
            break
    scenic_arount.append(score)
    score = 0

    for k in range(j-1,-1,-1):
        score += 1
        if map[i][k]>=height:
            break
    scenic_arount.append(score)
    score = 0
    for k in range(j+1,len(map[0])):
        score += 1
        if map[i][k]>=height:
            break
    scenic_arount.append(score)
    return math.prod(scenic_arount)

def part1(map):
    around = (2*len(map)+2*len(map[0])-4)
    npmap = np.array(map)
    for i in range(1,len(npmap)-1):
        for j in range(1,len(npmap[i])-1):
            if is_visible(npmap,i,j):
                around+=1
    return around

def part2(map):
    around=[]
    for i in range(1,len(map)-1):
        for j in range(1,len(map[i])-1):
            around.append(scenic_score(map,i,j))
    return max(around)

def test(demo_file):
    assert part1(read_map(demo_file)) == 21
    assert part2(read_map(demo_file)) == 8

if __name__ == "__main__":
    test("demo8.txt")
    part1 = part1(read_map("day8.txt"))
    part2 = part2(read_map("day8.txt"))
    print(f"Result for part 1 is {part1}")
    print(f"Result for part 2 is {part2}")
