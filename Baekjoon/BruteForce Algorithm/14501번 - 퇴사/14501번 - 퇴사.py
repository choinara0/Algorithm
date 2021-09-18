import sys

N = int(sys.stdin.readline())
table = []
answer = 0
for i in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))
# print(table)

def bruteForce(day, pay):
    global answer
    # print(day, pay)
    if day >= N:
        if day == N:
            total = sum(pay)
        else:
            total = sum(pay[:-1])

        if total > answer:
            answer = total
        return
    bruteForce(day+1, pay)
    nday, npay = day+table[day][0], pay+[table[day][1]]
    bruteForce(nday, npay)

bruteForce(0, [])
print(answer)
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200