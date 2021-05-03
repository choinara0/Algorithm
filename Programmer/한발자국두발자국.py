'''
문제 개요
n개의 계단이 있습니다. 한 발자국에 한계단이나 두계단을 오를 수 있습니다. 계단 꼭대기까지 오르려면 얼마나 많은 방법으로 오를 수 있을까요?

입출력 형식
입력 : n (계단의 수)
출력 : 계단을 오르는 경우의 수
입출력 예
예 1)
Input : 2
Output : 2
총 두가지 방법으로 오를 수 있다.
한계단 + 한계단
두계단
'''

def solution(n):
    current_num = 0
    next_num = 1
    for i in range(n+1):
        current_num, next_num = next_num, current_num + next_num
    return current_num

