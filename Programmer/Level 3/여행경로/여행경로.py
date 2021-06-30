
def solution(tickets):
    answer = []
    path = dict()
    for i in tickets:
        if i[0] not in path:
            path[i[0]] = [i[1]]
        else:
            path[i[0]].append(i[1])
    for i in path.keys():
        path[i].sort(reverse=True)
    stack = ["ICN"]

    while(stack):
        top = stack[-1]
        if top not in path or len(path[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(path[top][-1])
            path[top].pop()
    answer.reverse()
    print(answer)
    return answer

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

