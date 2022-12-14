import matplotlib.pyplot as plt
import imageio as imageio
import numpy as np

GIF=500
INLINEDRAW=False
EXT="png"

start_point=(500,0)

def read_map(efl_file):
    with open(efl_file, 'r') as f:
        map = [line.replace("\n", "") for line in f.readlines()]
    return map

def expand(x1,y1,x2,y2):
    if x1==x2:
        return [(x1,i) for i in range(min(y1,y2),max(y1,y2)+1)]
    if y1==y2:
        return [(i,y1) for i in range(min(x1,x2),max(x1,x2)+1)]

def construct8block(line):
    walls=line.split("->")
    wall_coord=[]
    start=walls[0]
    for wall in walls[1:]:
        wall_coord.extend(expand(int(start.split(",")[0]),int(start.split(",")[1]),int(wall.split(",")[0]),int(wall.split(",")[1])))
        start=wall
    return wall_coord

def construct_map(map_file):
    map=[]
    lines = read_map(map_file)
    for line in lines:
        map.extend(construct8block(line))
    print(len(map))
    maxy = sorted(map,key=lambda x: x[1],reverse=True)[0][1]
    maxx=start_point[0]+maxy+20
    npmap=np.zeros((maxx,maxy+3))
    for i in map:
        npmap[i[0],i[1]]=1
    return npmap

def next_position(map,position):
    if map[position[0]][position[1]+1]==0:
        return (position[0],position[1]+1)
    if map[position[0]-1][position[1]+1]==0:
        return (position[0]-1,position[1]+1)
    if map[position[0]+1][position[1]+1]==0:
        return (position[0]+1,position[1]+1)
    return None

def next_position2(map,position):
    if position[1] == len(map[0])-2:
        return None
    if map[position[0]][position[1]+1]==0:
        return (position[0],position[1]+1)
    if map[position[0]-1][position[1]+1]==0:
        return (position[0]-1,position[1]+1)
    if map[position[0]+1][position[1]+1]==0:
        return (position[0]+1,position[1]+1)
    if position[1] == 0:
        return -1
    return None

def sand(map,start_position):
    position=start_position
    sand=0

    while(position[1]<(len(map[0])-1)):
        position_inter=next_position(map,position)
        if position_inter is None:
            if sand % 100 == 0:
                print(".", end="")
            if GIF!=False:
                if sand%(GIF//10)==0:
                    filename = f'{sand}.{EXT}'
                    filenames.append(filename)
                    plt.imshow(map.T[0:160, 400:550])
                    plt.savefig(filename)
            sand+=1
            map[position[0]][position[1]]=2
            position=start_position
        else:
            position=position_inter
    return sand,map

def sand2(map,start_position):
    position=start_position
    sand=0
    while(position!=-1):
        position_inter=next_position2(map,position)
        if position_inter is None:
            if sand % 100 == 0:
                print(".", end="")
            if GIF:
                if sand%GIF==0:
                    filename = f'{sand}.{EXT}'
                    filenames.append(filename)
                    plt.imshow(map.T[0:165, 320:680])
                    plt.savefig(filename)
            sand+=1
            map[position[0]][position[1]]=2
            position=start_position
        else:
            position=position_inter
    return sand+1,map

def draw(map,part=1):
    if INLINEDRAW:
        plt.imshow(map.T[0:165, 320:680])
        plt.show()

    if GIF:
        with imageio.get_writer(f'mygif-part{part}.gif', mode='I') as writer:
            for filename in filenames:
                image = imageio.v2.imread(filename)
                writer.append_data(image)
        import os
        for filename in set(filenames):
            os.remove(filename)

filenames = []
def part1(filename):
    filenames = []
    global_map = construct_map(filename)
    result,map = sand(global_map, start_point)
    draw(map)
    return result


def part2(filename):

    global_map = construct_map(filename)
    result,map = sand2(global_map, start_point)
    draw(map,2)
    return result

def test(demo_file):
    pass
    assert part1(demo_file) == 24
    assert part2(demo_file) == 93

if __name__ == "__main__":
    test("demo14.txt")
    filenames = []
    part1 = part1("day14.txt")
    filenames = []
    part2 = part2("day14.txt")
    print("")
    print(f"Result for part 1 is {part1}")
    print(f"Result for part 2 is {part2}")
