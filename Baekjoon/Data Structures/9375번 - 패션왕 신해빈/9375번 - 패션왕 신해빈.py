import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    clothes = {}
    for i in range(n):
        name, type = map(str, sys.stdin.readline().split())
        if type in clothes:
            clothes[type].append(name)
        else:
            clothes[type] = [name]

    count = 1
    for k in clothes:
        count *= len(clothes[k])+1
    count -= 1
    print(count)