import sys
input = sys.stdin.readline

def factorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

def permu(selected, i):
    global cnt
    if i == len(s):
        cnt += 1
        if cnt == k:
            return selected
    else:
        for c in s:
            if c not in selected:
                r = permu(selected+c, i+1)
                if r:
                    return r


while True:
    try:
        s, k = input().split()
    except:
        break
    k = int(k)
    l = factorial(len(s))
    cnt = 0
    state = False
    if k > l:
        print('{} {} = No permutation'.format(s, k))
    else:
        print('{} {} = {}'.format(s, k, permu('', 0)))