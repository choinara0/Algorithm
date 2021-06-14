def check_div(n):
    cnt = 0
    for i in range(1, n+1):
        if n%i==0:
            cnt += 1
    return cnt


def solution(left, right):
    answer = 0
    nums = [i for i in range(left, right+1)]
    div_cnt = [0 for i in range(left, right + 1)]

    for i in range(len(nums)):
        div_cnt[i] = check_div(nums[i])
    for i in range(len(nums)):
        if div_cnt[i]%2==0:
            answer+=nums[i]
        else:
            answer-=nums[i]

    return answer

solution(24, 27)