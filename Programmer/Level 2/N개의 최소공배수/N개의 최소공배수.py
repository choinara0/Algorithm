'''
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
[2,6,8,14]	168
[1,2,3]	6

최소공배수는 두 수의 곱을 최대 공약수로 나눈 값과 같다!!!!

'''

def gcd(a,b):
    a, b = max(a, b), min(a,b)
    while b>0:
        a,b = b, a%b
    return a

def solution(arr):
    while len(arr) != 1:
        a = arr.pop()
        b = arr.pop()
        c = gcd(a,b)
        arr.insert(0, int(a*b/c))
    answer = arr[0]

    return answer
