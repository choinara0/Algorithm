import sys

def dfs(depth, score, a1, a2, a3):
    global answer
    if depth == 10:
        if score >= 5:
            answer += 1
        return

    for i in range(1, 6):
        if a2 == a3 == i:
            continue
        dfs(depth+1, score + (i==answer_list[depth]), a2, a3, i)

    return

answer_list = list(map(int, sys.stdin.readline().split()))
answer = 0
dfs(0, 0, 0, 0, 0)
print(answer)