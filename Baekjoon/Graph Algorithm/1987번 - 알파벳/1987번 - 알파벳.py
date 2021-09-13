import sys

def bfs():
    answer = 1
    queue = set([(0, 0, matrix[0][0])])

    while queue:
        x, y, visited = queue.pop()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if ((0<=new_x<R) and (0<=new_y<C)) and matrix[new_x][new_y] not in visited:
                next_visited = visited + matrix[new_x][new_y]
                queue.add((new_x, new_y, next_visited))
                answer = max(answer, len(next_visited))

    return answer

R, C = map(int, sys.stdin.readline().split())
matrix = []
for i in range(R):
    matrix.append(list(sys.stdin.readline()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())

