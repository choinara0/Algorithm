import sys

N = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())
tree = [[] for i in range(N+1)]
root = -1
cnt = 0

def dfs(node):
    global cnt
    if not tree[node]:
        cnt += 1
        return
    for n in tree[node]:
        dfs(n)

for i in range(len(parent)):
    if parent[i] == -1:
        root = i
        continue
    if i == delete_node:
        continue
    else:
        tree[parent[i]].append(i)

if root != delete_node:
    dfs(root)
print(cnt)