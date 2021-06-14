def solution(numbers, target):
    answer = 0
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            else:
                return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
        # print("idx : ", idx, "result : ", result)
    dfs(0,0)
    # print(answer)
    return answer

solution([1,1,1,1,1], 3)