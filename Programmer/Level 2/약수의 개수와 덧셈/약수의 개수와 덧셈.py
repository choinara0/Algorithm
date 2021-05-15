'''
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
입출력 예
left	right	result
13	17	43
24	27	52
'''


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