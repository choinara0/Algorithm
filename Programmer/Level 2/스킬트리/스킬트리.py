from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        s = skill_trees[i]
        deque1 = deque(skill)
        for j in range(len(s)):
            if s[j] in skill:
                x = deque1.popleft()
                if x != s[j]:
                    break

            if j == len(s)-1:
                answer+=1
    print(answer)
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])