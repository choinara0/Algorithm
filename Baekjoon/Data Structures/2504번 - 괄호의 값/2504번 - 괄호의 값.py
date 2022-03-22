import sys

input_string = list(map(str, sys.stdin.readline().strip()))
stack = []
temp = 1
answer = 0

for i in range(len(input_string)):
    if input_string[i] == '(':
        temp *= 2
        stack.append(input_string[i])
    elif input_string[i] == '[':
        temp *= 3
        stack.append(input_string[i])
    elif input_string[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if input_string[i-1] == '(':
            answer += temp
        temp //= 2
        stack.pop()

    elif input_string[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if input_string[i-1] == '[':
            answer += temp
        temp //= 3
        stack.pop()

if stack:
    answer = 0
print(answer)