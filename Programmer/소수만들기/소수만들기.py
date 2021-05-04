from itertools import combinations


def check(a, b, c):
    sum = a + b + c
    for i in range(2, sum):
        if sum % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for i in A:
        if check(i[0], i[1], i[2]):
            answer += 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer
