
import math


def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    for row in range(sum, 2, -1):
        if sum % row == 0:
            col = sum // row
            if yellow == (row - 2) * (col - 2):
                answer.append(row)
                answer.append(col)
                break

    return answer


solution(10, 2)
solution(8, 1)
solution(24, 24)

