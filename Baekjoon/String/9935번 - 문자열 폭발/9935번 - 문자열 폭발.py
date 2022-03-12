import sys

word = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []

for char in word:
    stack.append(char)

    if char == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        for i in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')