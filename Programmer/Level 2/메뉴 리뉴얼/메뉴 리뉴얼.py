from itertools import combinations

def solution(orders, course):
    answer = []
    order_list = list()
    order_dict = dict()
    for i in range(len(orders)):
        for j in range(2, len(orders[i])+1):
            temp = list(combinations(orders[i], j))
            order_list.append(temp)

    for i in range(len(order_list)):
        for j in range(len(order_list[i])):
            temp = ''.join(sorted(order_list[i][j]))
            if temp in order_dict:
                order_dict[temp] += 1
            else:
                order_dict[temp] = 1

    sorted_menu = sorted(order_dict.items(), key=lambda x:[len(x[0]), x[1]])
    for i in course:
        temp = []
        max = 1
        cnt = 0
        for j in range(len(sorted_menu)):
            if len(sorted_menu[j][0]) == i:
                temp.append(sorted_menu[j])
                if sorted_menu[j][1] > max:
                    max = sorted_menu[j][1]
        while temp:
            if temp[cnt][1] < max or max==1:
                temp.pop(cnt)
            else:
                answer.append(temp[cnt][0])
                temp.pop(cnt)

    return sorted(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
solution(["XYZ", "XWY", "WXA"], [2,3,4])