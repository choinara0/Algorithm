def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        if a < b: a, b = b, a
        answer.append(a + 1)
    return answer

solution(3, 2, 5) #[3,2,2,3]
solution(4, 7, 14) #[4,3,3,3,4,4,4,4]