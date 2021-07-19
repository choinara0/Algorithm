
def solution(clothes):
    answer = 1
    table = {}

    for val, key in clothes:
        if key in table.keys():
            table[key].append(val)
        elif key not in table.keys():
            table[key] = [val]

    print(table)

    for val in table.values():
        answer *= (len(val) + 1)
    answer -= 1
    return answer

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])