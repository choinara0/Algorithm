from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in range(len(info)):
        temp = info[i].split()
        info_key = int(temp[-1])
        info_val = temp[:-1]

        for j in range(5):
            for k in combinations(info_val, j):
                temp_val = ''.join(k)
                info_dict[temp_val].append(info_key)

    for k in info_dict.keys():
        info_dict[k].sort()
    for i in range(len(query)):
        temp = query[i].split()
        query_key = int(temp[-1])
        query_val = temp[:-1]

        for j in range(3):
            query_val.remove('and')
        while '-' in query_val:
            query_val.remove('-')

        query_val = ''.join(query_val)


        if query_val in info_dict:
            score = info_dict[query_val]
            if len(score) > 0:
                start, end = 0, len(score)
                while(end > start):
                    mid = (start + end) // 2
                    # print(start, mid, end, score[mid], query_key)
                    if score[mid] >= query_key:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(score) - start)

        else:
            answer.append(0)

    return answer


""" 
정확성만 통과하고 효율성은 통과 X
def solution(info, query):
    answer = []
    info_split = []
    query_split= []
    for i in range(len(info)):
        info_split.append(info[i].split())

    for i in range(len(query)):
        temp = query[i].split()
        temp2= []
        for j in range(len(temp)):
            if temp[j] != 'and':
                temp2.append(temp[j])
        query_split.append(temp2)

    for i in range(len(query_split)):
        temp = 0
        info_index = 0
        while (info_index < len(info_split)):
            for j in range(len(query_split)):
                if j == 4 and int(query_split[i][j]) <= int(info_split[info_index][j]):
                    temp += 1
                    break
                if query_split[i][j] != '-' and info_split[info_index][j] != query_split[i][j]:
                    break
            info_index += 1
        answer.append(temp)
    return answer
"""

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])