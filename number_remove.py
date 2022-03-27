from collections import deque

def solution(n, board):
    visited = []

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([[0, 0]])

    count = 0
    current = 1

    while q:
        x, y = q.popleft()
        if current == (n ** 2) + 1:
            break

        if [x, y] in visited:
            continue

        visited.append([x, y])
        count += 1

        if board[x][y] == current:
            current += 1
            count += 1
            visited = []

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == n:
                nx = 0
            if nx == -1:
                nx = n - 1
            if ny == n:
                ny = 0
            if ny == -1:
                ny = n - 1

            q.append([nx, ny])

    return count

print(solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]	))
print(solution(2, [[2, 3], [4, 1]]	))
print(solution(4, [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]]	))