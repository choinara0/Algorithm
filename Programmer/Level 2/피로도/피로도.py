from itertools import permutations
def solution(k, dungeons):
    answer = 0

    for perm in permutations(dungeons, len(dungeons)):
        num = k
        result = 0
        for p in perm:
            if num >= p[0] and num - p[1] >= 0:
                num -= p[1]
                result += 1
        if result > answer:
            answer = result

    return answer

solution(80, [[80,20],[50,40],[30,10]]) # 3