import sys
from collections import deque

word = list(map(str, sys.stdin.readline().strip()))
answer = ''
check = True
in_stack = deque()
out_stack = []
for i in word:
    if i == '<':
        while out_stack:
            answer += out_stack.pop()
        in_stack.append(i)
        check = False
    elif i == '>':
        in_stack.append(i)
        check = True
        while in_stack:
            answer += in_stack.popleft()
    elif i == ' ':
        if check:
            while out_stack:
                answer += out_stack.pop()
            answer += ' '
        else:
            while in_stack:
                answer += in_stack.popleft()
            answer += ' '
    else:
        if check:
            out_stack.append(i)
        else:
            in_stack.append(i)

while out_stack:
    answer += out_stack.pop()

print(answer)