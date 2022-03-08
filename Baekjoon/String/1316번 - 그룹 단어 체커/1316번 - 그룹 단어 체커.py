import sys

N = int(sys.stdin.readline())
answer = N

for _ in range(N):
    visited = [0] * 26
    word = sys.stdin.readline().strip()

    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                answer -= 1
                break
print(answer)