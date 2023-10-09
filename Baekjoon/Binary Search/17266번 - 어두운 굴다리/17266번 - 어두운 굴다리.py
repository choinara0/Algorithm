import sys

def bs(p, m):
    if p[1] - p[0] > m: #굴다리 사이의 거리가 mid보다 크면 다 비출 수 없음
        return 0
    if p[-1] - p[-2] > m: #굴다리 사이의 거리가 mid보다 크면 다 비출 수 없음
        return 0
    for i in range(1, len(p)-2):
        if(p[i+1] - p[i]) // 2 > m:
            return 0
    return 1

N = int(sys.stdin.readline()) #굴다리의 길이
M = int(sys.stdin.readline()) #굴다리의 개수
position = [0] + list(map(int, sys.stdin.readline().split())) + [N] #가로등의 위치, 가로등이 한개일때를 위해 양쪽에 추가

# 아이디어
# left = 0, right = N, mid = (left + rigth )// 2 로 했을 때
# mid값이 다 굴다리를 밝힐 수 있으면 right -1
# mid값이 굴다리를 밝힐 수 없으면 left + 1

left, right = 0, N
answer = 0

while left <= right:
    mid = (left + right) // 2

    if bs(position, mid): #
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)