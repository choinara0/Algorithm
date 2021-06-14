def solution(A, B):
    answer = 0
    a = sorted(A)
    b = sorted(B)
    tmp = 0
    for i in range(len(a)):
        for j in range(tmp, len(b)):
            if a[i] < b[j]:
                answer += 1
                b.remove(b[j])
                tmp = j
                break

    return answer