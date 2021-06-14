def solution(record):
    answer = []
    id_nickname = {}
    for i in range(len(record)):
        a = record[i].split()
        if a[0] == "Enter":
            if a[1] in id_nickname:
                id_nickname[a[1]] = a[2]
            else:
                id_nickname[a[1]] = a[2]
        if a[0] == "Change":
            id_nickname[a[1]] = a[2]

    print(id_nickname)
    for i in range(len(record)):
        a = record[i].split()
        if a[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(id_nickname[a[1]]))
        elif a[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(id_nickname[a[1]]))

    print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])