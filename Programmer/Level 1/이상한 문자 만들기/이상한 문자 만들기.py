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

