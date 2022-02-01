import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    parent = [0] * (N+1)

    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        parent[b] = a

    target_a, target_b = map(int, sys.stdin.readline().split())
    parent_target_a, parent_target_b = [0, target_a], [0, target_b]

    while parent[target_a]:
        parent_target_a.append(parent[target_a])
        target_a = parent[target_a]

    while parent[target_b]:
        parent_target_b.append(parent[target_b])
        target_b = parent[target_b]

    idx = 1
    while parent_target_a[-idx] == parent_target_b[-idx]:
        idx += 1

    print(parent_target_a[-idx + 1])