
def solution(x):
    answer = True
    str_n = str(x)
    sum = 0
    for i in str_n:
        sum += int(i)
    if x%sum==0:
        answer = True
    else:
        answer = False
    return answer