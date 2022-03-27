# 뱀이 나와서 기어다니는 데, 사과를 먹으면 먹을 수록 뱀의 길이가 늘어난다.
# 벽 또는 자기자신과 부딪히면 게임은 끝남.

# 뱀은 매초 이동 하는데, 다음과 같은 규칙을 따름.
# 1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치 시킨다.
# 2. 사과가 있다면, 그 칸에 있던 사과는 없어지고 꼬리는 움직이지 않는다.
# 3. 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. (몸 길이는 변하지 않는다.)
# = 사과의 위치와 뱀의 위치가 주어졌을 때, 이 게임이 몇 초에 끝나는지 계산하라


def is_move(table, x, y, limit):
    return (0 <= x < limit) and (0 <= y < limit) and table[x][y] != -1


def change_direction(x, y, d):
    # 90도 회전, D = right, L = left

    if x == 0 and y == 1:
        # 현재 right
        if d == 'D':
            x, y = 1, 0
        else:
            x, y = -1, 0
    elif x == 1 and y == 0:
        # 현재 down
        if d == 'D':
            x, y = 0, -1
        else:
            x, y = 0, 1
    elif x == 0 and y == -1:
        # 현재 left
        if d == 'D':
            x, y = -1, 0
        else:
            x, y = 1, 0
    else:
        # 현재 up
        if d == 'D':
            x, y = 0, 1
        else:
            x, y = 0, -1
    return [x, y]


map_size = int(input())
apple_count = int(input())
turn = [0] * 10001

apple_point = []
snake_move_action = []

for a in range(apple_count):
    p1, p2 = input().split(' ')
    apple_point.append((int(p1), int(p2)))

snake_move_count = int(input().strip())

for i in range(snake_move_count):
    second, direction = input().strip().split(' ')
    turn[int(second)] = direction

table = [[0 for i in range(map_size)] for j in range(map_size)]
for i in apple_point:
    p1, p2 = i
    table[int(p1) - 1][int(p2) - 1] = 1

snake = [[0, 0]]
snake_head = [0, 0]
table[0][0] = -1
d = [0, 1]

count = 1

while True:
    dx = snake_head[0] + d[0]
    dy = snake_head[1] + d[1]

    if not is_move(table, dx, dy, map_size):
        break

    # 스네이크를 이동시킴
    snake_head[0] = dx
    snake_head[1] = dy

    # 해당 좌표에 사과가 없을 경우,
    if table[dx][dy] != 1:
        tail = snake[0]
        table[tail[0]][tail[1]] = 0
        snake.pop(0)

    if turn[count]:
        d[0], d[1] = change_direction(d[0], d[1], turn[count])

    table[dx][dy] = -1
    snake.append([dx, dy])

    count += 1

print(count)