# def solution(s):
#     answer = ""
#     num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
#     start = 0
#
#     for i in range(1, len(s)+1):
#         for k, v in num.items():
#             if s[start:i] == k:
#                 answer += v
#                 start = i
#             elif s[start:i] == v:
#                 answer += v
#                 start = i
#
#     return int(answer_

def solution(s):

    num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
           "eight": "8", "nine": "9"}

    for k, v in num.items():
        s = s.replace(k, v)

    return int(s)


solution("one4seveneight")

