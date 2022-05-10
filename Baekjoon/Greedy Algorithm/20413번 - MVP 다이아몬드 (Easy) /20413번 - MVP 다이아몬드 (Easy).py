import sys
input = sys.stdin.readline

N = int(input())
ref = list(map(int, input().split()))
grades = input().strip()
answer = 0
prev = 0

for i in range(N):
    if grades[i] == 'B':
        answer += ref[0] - 1 - prev
        prev = ref[0] - 1 - prev
    elif grades[i] == 'S':
        answer += ref[1] - 1 - prev
        prev = ref[1] - 1 - prev
    elif grades[i] == 'G':
        answer += ref[2] - 1 - prev
        prev = ref[2] - 1 - prev
    elif grades[i] == 'P':
        answer += ref[3] - 1 - prev
        prev = ref[3] - 1 - prev
    elif grades[i] == 'D':
        answer += ref[3]
        prev = ref[3]

print(answer)
