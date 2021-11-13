import sys
def check():
    money = 0
    num = 0
    for data in datas:
        if mid < data:
            return M+1
        if money >= data:
            money -= data
        else:
            money = mid - data
            num+=1
    return num


N, M = map(int, input().split())
datas = [int(input()) for _ in range(N)]
low = 0
high = sys.maxsize
answer = sys.maxsize
while(low <= high):
    mid = (low+high)//2
    res = check()
    if res > M:
        low = mid + 1
    elif res<= M:
        answer = min(answer, mid)
        high = mid - 1
print(answer)