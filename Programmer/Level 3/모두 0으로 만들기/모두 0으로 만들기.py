import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
answer = 0

def dfs(x, a, tree, visited):
    global answer
    visited[x] = 1

    for node in tree[x]:
        if not visited[node]:
            a[x] += dfs(node, a, tree, visited)

    answer += abs(a[x])

    return a[x]

def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    tree = defaultdict(list)

    for node1, node2 in edges:
        tree[node1].append(node2)
        tree[node2].append(node1)

    visited = [0] * len(a)

    dfs(0, a, tree, visited)

    return answer

solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]) #9
solution([0,1,0], [[0,1],[1,2]]) #-1