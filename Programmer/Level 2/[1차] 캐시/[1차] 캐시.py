from collections import deque
def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5


    q = deque()
    for i in cities:
        i = i.lower()
        if i in q:
            answer += 1
        else:
            answer += 5

        if i in q:
            q.remove(i)
            q.append(i)
        else:
            if len(q) >= cacheSize:
                q.popleft()
            q.append(i)
    print(answer)
    return answer

solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])