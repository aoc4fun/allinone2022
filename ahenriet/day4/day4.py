def intersect_method_1(first_set,second_set):
    return second_set.issubset(first_set) and len(first_set)==len(first_set.union(second_set))

def intersect_method_2(first_set,second_set):
    return len(first_set)+len(second_set)!=len(first_set.union(second_set))

def overloap_compute(efl_file, intersect_method=intersect_method_1):
    with open(efl_file, 'r') as f:
        games = [x.replace("\n", "") for x in f.readlines()]
        count=0
        for game in games:
            stage1,stage2=game.split(",")
            first=set(list(range(int(stage1.split("-")[0]),int(stage1.split("-")[1])+1)))
            second=set(list(range(int(stage2.split("-")[0]),int(stage2.split("-")[1])+1)))
            if len(first)<len(second):
                second,first=first,second
            count+=intersect_method(first,second)
        return count

assert(overloap_compute("demo4.txt")==2)
print(f"Result for part 1 is {overloap_compute('day4.txt')}")

assert(overloap_compute("demo4.txt",intersect_method=intersect_method_2)==4)
print(f"Result for part 2 is {overloap_compute('day4.txt',intersect_method=intersect_method_2)}")

