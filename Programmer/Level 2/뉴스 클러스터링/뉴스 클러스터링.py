def convert_dict(str):
    arr = []
    for i in range(len(str)-1):
        x = str[i]
        y = str[i+1]
        if ((ord(x) >= 65 and ord(x)<= 90) or (ord(x) >= 97 and ord(x)<= 122)) and \
                ((ord(y) >= 65 and ord(y)<= 90) or (ord(y) >= 97 and ord(y)<= 122)):
            arr.append(x.upper()+y.upper())

    dict_str = dict()
    for i in arr:
        if i in dict_str.keys():
            dict_str[i] += 1
        else:
            dict_str[i] = 1
    return dict_str

def find_union(dict1, dict2):
    union_dict = dict()
    for k2, v2 in dict2.items():
        union_dict[k2] = v2
    for k1, v1 in dict1.items():
        if k1 in union_dict.keys():
            if v1 > union_dict[k1]:
                union_dict[k1] = v1
        else:
            union_dict[k1] = v1

    return union_dict

def find_intersection(dict1, dict2):
    intersection_dict = dict()
    for k1, v1 in dict1.items():
        if k1 in dict2.keys():
            if v1 < dict2[k1]:
                intersection_dict[k1] = v1
            else:
                intersection_dict[k1] = dict2[k1]
    return intersection_dict


def solution(str1, str2):
    answer = 0
    dict1 = convert_dict(str1)
    dict2 = convert_dict(str2)

    if len(dict1)==0 and len(dict2) ==0:
        return 65536

    union_dict = find_union(dict1, dict2)
    intersection_dict = find_intersection(dict1, dict2)

    answer = int((sum(intersection_dict.values()) / sum(union_dict.values())) * 65536)

    return answer

solution('FRANCE', 'french') #16384
solution('handshake', 'shake hands')#65536
solution('aa1+aa2', 'AAAA12') #43690
solution('E=M*C^2', 'e=m*c^2') #65536

