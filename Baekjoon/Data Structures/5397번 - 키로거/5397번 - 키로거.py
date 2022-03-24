import sys

T = int(sys.stdin.readline())

for _ in range(T):
    L = sys.stdin.readline().rstrip()
    left, right = [], []

    for x in L:
        if x == '-':
            if left:
                left.pop()
        elif x == '<' :
            if left:
                right.append(left.pop())
        elif x == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(x)
    print(''.join(left)+''.join(reversed(right)))