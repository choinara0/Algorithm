def solution(rows, columns, queries):
    table = []
    answer = []
    for i in range((rows)):
        table.append([a for a in range(i*columns+1, (i+1)*columns+1)])
    for query in queries:
        query = [x - 1 for x in query]
        tmp = table[query[0]][query[1]]
        small = tmp

        # left
        for i in range(query[0] + 1, query[2] + 1):
            table[i - 1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1] + 1, query[3] + 1):
            table[query[2]][i - 1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2] - 1, query[0] - 1, -1):
            table[i + 1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3] - 1, query[1] - 1, -1):
            table[query[0]][i + 1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1] + 1] = tmp
        answer.append(small)

    return answer

solution(6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]) #[8, 10, 25]
solution(3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]) #[1, 1, 5, 3]
solution(100,	97,	[[1,1,100,97]]) #[1, 1, 5, 3, 1]