# 케이스를 나눠서 생각하기
# cnt가 증가하는 케이스는 한 점은 안에 있고, 한 점은 밖에 있을 떄.
# 그림에서 아무런 행성이 없고 도착점에 있는 행성 하나가 주워졌을 떄를 생각해보자
# 출발점은 행성 밖에 있고, 도착점은 행성 안에 있으므로 cnt가 1이 증가한다.
# 점과 점 사이의 공식은 √(x1-x2)**2 + (y1-y2)**2 라고 한다.
# 즉 d1과 d2중 둘 중 하나만 cr보다 작은 경우만 cnt가 증가한다.

import sys
import math

T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    cnt = 0

    for _ in range(n):
        cx, cy, cr = map(int, sys.stdin.readline().split())
        d1 = math.sqrt(((x1-cx) ** 2 + (y1-cy) ** 2)) #출발점과 행성 중심과의 거리
        d2 = math.sqrt((x2-cx) ** 2 + (y2-cy) ** 2) #도착점과 행성 중심과의 거리

        if (d1 < cr and d2 > cr) or (d1 > cr and d2 < cr):
            cnt += 1

    print(cnt)
