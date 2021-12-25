'''import sys
caseCnt = 0
while True:
    caseCnt += 1
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    day = 0
    while True:
        if V >= P:
            V -= P
            day += L
        elif P >= V >= L:
            V -= V
            day += L
        else:
            day += V
            break

    print('Case ' + str(caseCnt) + ': ' + str(day))'''

import sys
caseCnt = 0
while True:
    caseCnt += 1
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    a = V // P
    b = V % P
    if L < b:
        b = L
    print("Case %d: %d" %(caseCnt, a*L+b))