import sys

M = int(sys.stdin.readline())
bit = 0

def add(bit, x):
    returnBit = bit | (1 << x)

    return returnBit

def remove(bit, x):
    returnBit = bit & ~(1 << x)

    return returnBit

def check(bit, x):
    if bit & (1 << x) == 0:
        return 0
    else:
        return 1

def toggle(bit, x):
    returnBit = bit ^ (1 << x)

    return returnBit

def all():
    returnBit = (1 << 20) - 1

    return returnBit

def empty():
    returnBit = 0

    return returnBit

for i in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'empty':
        bit = empty()
    elif command[0] == 'all':
        bit = all()
    else:
        op = command[0]
        num = int(command[1]) -1

        if op == 'add':
            bit = add(bit, num)
        elif op == 'remove':
            bit = remove(bit, num)
        elif op == 'toggle':
            bit = toggle(bit, num)
        elif op == 'check':
            print(check(bit, num))