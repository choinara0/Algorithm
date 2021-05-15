'''
문제 설명
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

제한 사항
n은 1,000,000 이하의 자연수 입니다.
입출력 예
n	result
78	83
15	23
'''

def solution(n):
    answer = 0
    bin_n = str(bin(n))[2:]
    sum_bin_n = 0
    for i in range(len(bin_n)):
        if bin_n[i] == '1':
            sum_bin_n += 1

    print(bin_n)
    while(1):
        n = n+1
        bin_new_n = str(bin(n))[2:]
        sum_bin_new_n = 0
        print(bin_new_n)
        for i in range(len(bin_new_n)):
            if bin_new_n[i] == '1':
                sum_bin_new_n += 1
        if sum_bin_new_n == sum_bin_n:
            answer = n
            break
    print(answer)
    return answer

solution(15)