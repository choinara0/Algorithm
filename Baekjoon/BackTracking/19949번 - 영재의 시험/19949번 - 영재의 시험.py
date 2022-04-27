import sys

def dfs(depth):
    global answer
    if depth == 10:
        score = 0
        for i in range(10):
            if result[i] == answer_list[i]:
                score += 1
        if score >= 5:
            answer += 1
        return

    for i in range(1, 6):
        if depth>1 and result[depth-1] == result[depth-2] == i:
            continue
        result.append(i)
        dfs(depth+1)
        result.pop()

    return

answer_list = list(map(int, sys.stdin.readline().split()))
result = []
answer = 0
dfs(0)
print(answer)