def solution(weights, head2head):
    answer = []
    info = []
    for i in range(len(weights)):
        if len(weights) - head2head[i].count('N') == 0:
            rate = 0
        else:
            rate = head2head[i].count('W') / (len(weights) - head2head[i].count('N'))
        win_count_weight = 0
        temp = list(head2head[i])
        for j in range(len(temp)):
            if temp[j] == 'W' and weights[i]<weights[j]:
                win_count_weight += 1
        info.append([i+1, weights[i], rate, win_count_weight])
    info.sort(key=lambda x:(-x[2], -x[3], -x[1], x[0]))
    for i in range(len(info)):
        answer.append(info[i][0])

    return answer

solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"])	#[3,4,1,2]
solution([145,92,86],["NLW","WNL","LWN"]) #[2,3,1]
solution([60,70,60],["NNN","NNN","NNN"]) #[2,1,3]