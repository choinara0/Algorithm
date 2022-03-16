import sys

n = int(sys.stdin.readline())
count = 0
stack = []
result = []
flag = False

for i in range(n):
    x = int(sys.stdin.readline())

    while count < x:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        flag = True
        break

if flag:
    print('NO')
else:
    print('\n'.join(result))