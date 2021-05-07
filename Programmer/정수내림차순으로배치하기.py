'''
문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.
입출력 예
n	return
118372	873211
'''

def solution(n):
    answer = 0
    list_n = []
    str_n = str(n)
    for i in str_n:
        list_n.append(i)
    list_n.sort(reverse=1)
    cnt = 1
    for i in list_n:
        answer += int(i)*(10**(len(list_n)-cnt))
        cnt+=1
    return answer

solution(132435)

'''
다른 사람 풀이

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
'''