import sys

N = int(sys.stdin.readline())
input_string = sys.stdin.readline().rstrip()
stack = []
word = {}
idx = 65
for i in range(N):
    word[chr(idx)] = int(sys.stdin.readline())
    idx += 1

for s in input_string:
    if s == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    elif s == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif s == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif s == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b/a)
    else:
        stack.append(word[s])

print('%.2f' %stack[0])
