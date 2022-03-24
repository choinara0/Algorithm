import sys

T = int(sys.stdin.readline())

for _ in range(T):
    L = sys.stdin.readline().rstrip()
    stack = []
    left_cnt = 0
    right_cnt = 0
    for i in range(len(L)):
        if L[i] == '-' and stack:
            stack.pop()
        elif L[i] == '<' and stack:
            left_cnt += 1
        elif L[i] == '>' and stack:
            right_cnt += 1
        else:
            if not stack:
                left_cnt = 0
                right_cnt = 0
                stack.append(L[i])
            else:
                
