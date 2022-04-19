def solution(board, skill):
    answer = 0
    # 누적합 기록 배열
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for sk in skill:
        type, r1, c1, r2, c2, degree = sk

        # 누적합 기록하기
        if type == 1:
            temp[r1][c1] -= degree
            temp[r1][c2+1] += degree
            temp[r2+1][c1] += degree
            temp[r2+1][c2+1] -= degree

        elif type == 2:
            temp[r1][c1] += degree
            temp[r1][c2+1] -= degree
            temp[r2+1][c1] -= degree
            temp[r2+1][c2+1] += degree

        # 행 기준 누적 합
    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i][j+1] += temp[i][j]

        # 열 기준 누적합
    for j in range(len(temp[0])-1):
        for i in range(len(temp)-1):
            temp[i+1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]) # 10
solution([[1,2,3],[4,5,6],[7,8,9]],	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]) # 6