from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)
    id_reported_by_me = defaultdict(set)
    num_reported = defaultdict(int)
    suspend = []

    for r in report:
        a, b = r.split()
        id_reported_by_me[a].add(b)
        num_reported[b] += 1

        if num_reported[b] == k:
            suspend.append(b)

    for s in suspend:
        for i in range(len(id_list)):
            if s in id_reported_by_me[id_list[i]]:
                answer[i] += 1

    return answer

solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2)
#[2,1,1,0]

solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"],	3)
#[0, 0]