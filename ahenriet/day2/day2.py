def find_score_1(efl_file):
    with open(efl_file, 'r') as f:
        games=[line.replace("\n","") for line in f.readlines()]
        result=[]
        for game in games:
            data=game.split(" ")
            result.append({"X": 1, "Y": 2, "Z": 3}[data[1]]+(ord(data[0])==(ord(data[1])-23))*3+6*(data[0]+data[1]in ["AY","BZ","CX"]))
        return sum(result)

def find_score_2(efl_file):
    with open(efl_file, 'r') as f:
        games=[line.replace("\n","") for line in f.readlines()]
        result=[]
        for game in games:
            data=game.split(" ")
            result.append(
                {"X": 0, "Y": 3, "Z": 6}[data[1]]
                +
                {
                    "A":{"X": 3, "Y": 1, "Z": 2},
                    "B":{"X": 1, "Y": 2, "Z": 3},
                    "C":{"X": 2, "Y": 3, "Z": 1}
                }[data[0]][data[1]]
            )
        return sum(result)

print(find_score_1("demo2.txt"))
print(find_score_1("day2.txt"))

print(find_score_2("demo2.txt"))
print(find_score_2("day2.txt"))
