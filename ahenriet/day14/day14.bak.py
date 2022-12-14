import numpy as np

start_point=(500,0)

def read_map(efl_file):
    with open(efl_file, 'r') as f:
        map = [line.replace("\n", "") for line in f.readlines()]
    return map

def expend(x1,y1,x2,y2):
    if x1==x2:
        return [(x1,i) for i in range(min(y1,y2),max(y1,y2)+1)]
    if y1==y2:
        return [(i,y1) for i in range(min(x1,x2),max(x1,x2)+1)]

def construct8block(line):
    walls=line.split("->")
    wall_coord=[]
    start=walls[0]
    for wall in walls[1:]:
        wall_coord.extend(expend(int(start.split(",")[0]),int(start.split(",")[1]),int(wall.split(",")[0]),int(wall.split(",")[1])))
        start=wall
    return wall_coord

def construct_map(map_file):
    map=[]
    lines = read_map(map_file)
    for line in lines:
        map.extend(construct8block(line))
    print(len(map))
    return map
    # maxx = sorted(map,key=lambda x: x[0],reverse=True)[0][0]
    # maxy = sorted(map,key=lambda x: x[1],reverse=True)[0][1]
    # maxx=500+maxy+20
    # np.zeros((maxx,maxy+3))
    # for i in map:
    #     np[i[0],i[1]]="#"
    # return np
def max_y(map):
    return sorted(map,key=lambda x: x[1],reverse=True)[0][1]

def print_map(map):
    print(map)
    minx= sorted(map,key=lambda x: x[0])[0][0]
    miny = sorted(map,key=lambda x: x[1])[0][1]
    maxx = sorted(map,key=lambda x: x[0],reverse=True)[0][0]
    maxy = sorted(map,key=lambda x: x[1],reverse=True)[0][1]
    for i in range(miny,maxy+2):
        for j in range(minx-1,maxx+2):
            if (j,i) in map:
                print("#",end="")
            else:
                print(".",end="")
        print()
    return (minx,miny,maxx,maxy)

def next_position(map,position):
    if (position[0],position[1]+1) not in map:
        return (position[0],position[1]+1)
    if (position[0]-1,position[1]+1) not in map:
        return (position[0]-1,position[1]+1)
    if (position[0]+1,position[1]+1) not in map:
        return (position[0]+1,position[1]+1)
    return None

max_y_global=0

def position_in_map(map,position):
    return position[1]<max_y_global


def sand(map,start_position):
    position=start_position
    sand=0
    while(position_in_map(map,position)):
        position_inter=next_position(map,position)
#        print(position,position_inter)
        if position_inter is None:
            sand+=1
            map.append(position)
#            print_map(map)
            position=start_position
        else:
            position=position_inter
    return sand

global_map=construct_map("day14.txt")

print(print_map(global_map))

max_y_global=max_y(global_map)+2

print(sand(global_map,start_point))


def part1(map):
    return None

def part2(map):
    return None

def test(demo_file):
    pass
#    assert part1(read_map(demo_file)) == 21
#    assert part2(read_map(demo_file)) == 8

if __name__ == "__main__":
    test("demo14.txt")
#    part1 = part1(read_map("day8.txt"))
##    part2 = part2(read_map("day8.txt"))
#    print(f"Result for part 1 is {part1}")
#    print(f"Result for part 2 is {part2}")
