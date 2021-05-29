'''
문제 설명
XX 회사에서는 사원들의 출퇴근을 관리하는 다음과 같은 무인 시스템이 있습니다.

1. 모든 사원은 사원증을 가지고 있습니다.
2. 모든 사원은 출퇴근 시 가지고 있는 회원증을 출퇴근 기록기에 태그를 해야 합니다.
3. 출퇴근 기록기에 기록된 기록은 회사의 중앙 컴퓨터에 실시간으로 모이게 됩니다.
현재 회사 컴퓨터에 있는 로그 파일 logs가 매개변수로 주어 졌을 때, 회사에 있는 사람의 사원 번호로 오름차순으로 정렬하여 return 하는 solution 함수를 작성하세요.

제한사항
logs는 [ 사원 번호 ] 형태의 리스트(List)로 주어진다.
사원 번호는 5자리(10,000~99,999)의 정수(Int)형으로 주어진다.
모든 사원은 자유롭게 회사를 여러 번 들어왔다 나갔다 할 수 있습니다.
로그의 기록은 1,000,000번 이하입니다.
입출력 예시
logs	result
[23160, 23240, 23173, 23243, 23173]	[23160, 23240, 23243]
'''
'''
빈병
빈병
def solution(n, c, x):
    sum = n
    bottle = n + c
    while bottle >= x:
        new = bottle // x
        bottle %= x
        bottle += new
        sum += new
    
    return sum
'''
'''
펠린드롬
팰린드ㅡ롬
def solution(n, m):
    cnt = 0
    for i in range(n, m+1):
        a = str(i)
        if a == a[::-1]:
            cnt += 1
    return cnt
'''
'''
하노이
def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end)
    print(start, end) 
    hanoi_tower(n-1, 6-start-end, end) 
    
n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)
'''

def solution(logs):
    answer = []
    logs.sort()
    cnt = 0
    while(cnt<=len(logs)):
        if cnt == len(logs)-1:
            answer.append(logs[-1])
            break
        if logs[cnt] != logs[cnt+1]:
            answer.append(logs[cnt])
        else:
            cnt += 1
        cnt += 1
        print(cnt)
    print(answer)
    return answer
solution([23160, 23240, 23173, 23243, 23173])