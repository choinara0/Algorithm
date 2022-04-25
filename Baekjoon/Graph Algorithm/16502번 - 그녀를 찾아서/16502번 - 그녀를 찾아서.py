import sys

input = sys.stdin.readline
time = int(input())
M = int(input())
graph = []

for _ in range(M):
    start, end, p = map(str, input().split())
    graph.append([(ord(start)-ord('A')), (ord(end)-ord('A')), float(p)])

answer = [0.25, 0.25, 0.25, 0.25]
while time:
    time -= 1
    temp = [0, 0, 0, 0]

    for u, v, w in graph:
        temp[v] += answer[u] * w

    answer = temp

for x in answer:
    print('%.2f' %(x*100))