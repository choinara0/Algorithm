def solution(people, limit):
    answer = 0
    people = sorted(people)
    start, end = 0, len(people)-1

    while (start<=end):
        if start == end:
            answer += 1
            break
        elif people[start] + people[end] <= limit:
            answer += 1
            start += 1
            end -= 1
            continue

        end -= 1
        answer += 1

    return answer
# 50 50 70 80
# 50 70 80
solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)
