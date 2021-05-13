'''
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
입출력 예
s	return
"try hello world"	"TrY HeLlO WoRlD"
'''
# def solution(s):
#     answer = ''
#     temp = s.split()
#     print(temp)
#     for i in range(len(temp)):
#         a = temp[i]
#         for j in range(len(temp[i])):
#             if j%2==0 or j==0:
#                 a[j].upper()
#                 print(a[j])
#             else:
#                 a[j].lower()
#                 print(a[j])
#         answer += a
#         answer += " "
#     print(answer)
#
#     return answer
#
# solution('try hello python')

def solution(s):
    answer = ''
    s_list = list(s)
    s_split = s.split()
    for i in range(len(s_split)):
        i_list = list(s_split[i])
        for j in range(len(i_list)):
           if j%2==0 :
               i_list[j] = i_list[j].upper()
           elif j%2==1:
               i_list[j] = i_list[j].lower()
        s_split[i] = "".join(i_list)

    answer = " ".join(s_split)
    print(answer)
    return answer
solution('try hello python')

