import itertools
def check_prime(n):
    m = int(n**0.5)
    if n<2:
        False
    else:
        for i in range(2, m+1):
            if n%i==0:
                return False
        return True


def solution(numbers):
    answer = 0
    arr = []
    for i in range(1, len(numbers)+1):
        tmp = list(map(''.join, itertools.permutations(numbers, i)))
        for j in list(set(tmp)):
            if check_prime(int(j)):
                arr.append(int(j))

    answer = len(set(arr))

    return answer

solution("031")


