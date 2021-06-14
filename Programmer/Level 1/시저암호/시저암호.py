

# def solution(s, n):
#     answer = ''
#     for i in s:
#         ord_s_i = ord(i)
#         new_s_i = ord(i) + n
#
#         if ord_s_i >= 65 and ord_s_i <= 90:
#             if new_s_i > 90:
#                 new_s_i -= 26
#                 answer += chr(new_s_i)
#             else:
#                 answer += chr(new_s_i)
#         elif ord_s_i >= 97 and ord_s_i <= 122:
#             if new_s_i > 122:
#                 new_s_i -= 26
#                 answer += chr(new_s_i)
#             else:
#                 answer += chr(new_s_i)
#         else:
#             answer += " "
#
#     return answer

# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 1
#         idx = i + 1
#         if i == len(prices)-1:
#             answer.append(0)
#             break
#         while(1):
#             if idx == len(prices)-1:
#                 answer.append(cnt)
#                 break
#             if prices[i] <=prices[idx]:
#                 cnt += 1
#                 idx += 1
#             else:
#                 answer.append(cnt)
#                 break
#     return answer
# solution([498, 501, 470, 489])
# solution([1,2,3,2,3])
import heapq

import heapq
def solution(coins, amount):
    answer = 0
    check = 0
    coins.sort()
    new_c = [-i for i in coins]
    heap_c = heapq.heapify(new_c)

    while(new_c):
        max_c = min(new_c)
        if amount + max_c >=0:
            amount = amount + max_c
            check += 1
        elif amount +max_c <= 0:
            new_c.pop(0)
        print(amount)
    print(check)
    return answer

solution([1,2,5], 11)

