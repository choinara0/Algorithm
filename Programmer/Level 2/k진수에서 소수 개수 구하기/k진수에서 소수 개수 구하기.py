def convert(n, k):
    result = ''
    while n > 0:
        n, m = divmod(n, k)
        result += str(m)
    return result[::-1]

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    convert_n = convert(n, k)
    for num in convert_n.split('0'):
        if num.isdigit():
            if is_prime(int(num)):
                answer += 1
    return answer

solution(437674, 3) #3
solution(110011, 10) #2