def solution(numbers):
    answer = []
    numbers_length = int(len(numbers))
    for i in range(numbers_length):
        for j in range(numbers_length):
            sum = numbers[i] + numbers[j]
            if i!=j and sum not in answer:
                answer.append(sum)
    answer.sort()
    print(answer)
    return answer

from itertools import combinations
def solution2(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))

    return sorted(answer)