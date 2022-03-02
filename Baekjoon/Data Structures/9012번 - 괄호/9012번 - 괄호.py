import sys

T = int(sys.stdin.readline())

for _ in range(T):
    input_data = list(map(str, sys.stdin.readline().strip()))
    stack = []

    for i in input_data:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')