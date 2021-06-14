'''
n 부 터 m까지의 수 중의 numbers 리스트 안에 있는 수의 배수들의 합을 return 하도록 solution 함수를 작성하세요.

제한 사항
1 ≤ n ＜ m ≤ 100,000
numbers 안에 있는 수는 2 이상 100,000 이하의 자연수입니다.
numbers 의 크기(개수)는 2 이상 1,000 이하입니다.
입출력 예
n	m	numbers	result
1	10	[3, 5]	33
입출력 예 설명
1부터 10까지의 수 중, 3 또는 5의 배수는 3, 5, 6, 9, 10이며 따라서 이 수들의 합은 33이다.

'''
def solution(n, m, numbers):
    answer = []

    for i in range(n, m+1):
        for j in range(len(numbers)):
            if i%numbers[j]==0:
                answer.append(i)
                break

    return sum(answer)

solution(1, 10, [3,5])