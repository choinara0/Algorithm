def solution(dirs):
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    d = {"U": 0, "L":1, "D":2, "R":3}
    visited = set()
    answer = 0
    x, y = 0, 0
    for dir in dirs:
        i = d[dir]
        nx, ny = x + dx[i], y + dy[i]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        if (x,y,nx,ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1
        x, y = nx, ny

    return answer

solution("ULURRDLLU") # 7
solution("LULLLLLLU") #7