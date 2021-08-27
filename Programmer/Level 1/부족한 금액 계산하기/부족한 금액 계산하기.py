def solution(price, money, count):
    sum = 0
    for i in range(1, count+1):
        sum += i*price
    if money >= sum:
        return 0
    else:
        return sum - money


solution(3, 20, 4) # 10