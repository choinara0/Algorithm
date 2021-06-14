def solution(n, m):
    answer = []
    num = [n,m]
    maxnum = max(num)
    최대공약수 = 1
    for i in range(1, maxnum+1):
        if n%i==0 and m%i==0:
            최대공약수 = i
    answer.append(최대공약수)
    최소공배수 = 0
    for i in range(maxnum, (n*m)+1):
        if i%n==0 and i%m==0:
            최소공배수 = i
            break
    answer.append(최소공배수)
    return answer