# from itertools import combinations
# numbers = [1, 2, 3, 4]
# a = list(combinations(numbers, 2))
# print(a)
#

# def solution(A, B):
#     answer = 0
#     new_B=[]
#     for i in range(len(A)):
#         n = 0
#         for j in range(len(B)):
#             if n==0 and A[i] < B[j]:
#                 n = B[j]
#             elif n!=0 and A[i] < B[j]:
#                 if n>B[j]:
#                     n = B[j]
#         if n!=0:
#             new_B.append(n)
#             B.remove(n)
#
#     print(new_B)
#     return answer

def solution(A, B):
    answer = 0
    a = sorted(A)
    b = sorted(B)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] <b[j]:
                answer += 1
                b.remove(b[j])
                break
    print(answer)
    return answer

solution([2,1,3,7], [2,2,6,8])
solution([2,2,2,2], [1,1,1,1])

1 3 5 7 9
2 2 4 5 7