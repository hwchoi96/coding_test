from collections import deque
dp = []

def get_shortest_path(table, src, des):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([src])
    visited = []

    while queue:
        x, y = queue.popleft()

        if x == des[0] and y == des[1]:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= des[0] and 0 <= ny <= des[1]:
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                    if table[nx][ny] == 'X':
                        return True

    # 최단 거리로 가는데에 중간에 막는게 없다면 거리두기를 지키지 않은 것임.
    return False

def is_good(table, person):
    dx = [-2, -1, -1, 0, 0, 1, 1, 2, -1, 0, 0, 1]
    dy = [0, -1, 1, 2, -2, 1, -1, 0, 0, 1, -1, 0]

    for i in range(len(dx)):
        if person[0] + dx[i] < 0 or person[1] + dy[i] < 0 or person[0] + dx[i] >= 5 or person[1] + dy[i] >= 5:
            continue

        if table[person[0] + dx[i]][person[1] + dy[i]] == 'P':
            # 인접 멘하탄 거리 내에 다른 사람이 존재할 때, BFS로 최단 경로를 구했을 때 파티션이 있으면 거리두기가 잘 된 것임.
            # if sorted([person, [person[0] + dx[i], person[1] + dy[i]]]) in dp:
            #     # 이미 계산한 결과가 있다면 검증하지 않음.
            #     continue
            #
            # dp.append(sorted([person, [person[0] + dx[i], person[1] + dy[i]]]))

            if not get_shortest_path(table, person, [person[0] + dx[i], person[1] + dy[i]]):
                return False

    return True

def check_other(table, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        if 0 <= x + dx[i] < 5 and 0 <= y + dy[i] < 5:
            nx = x + dx[i]
            ny = y + dy[i]

            if table[nx][ny] == 'P':
                return False

    return True

def check_block(table, x, y):
    count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        if 0 <= x + dx[i] < 5 and 0 <= y + dy[i] < 5:
            nx = x + dx[i]
            ny = y + dy[i]

            if table[nx][ny] == 'P':
                count += 1

    if count <= 1:
        return True
    else:
        return False

def solution(places):
    # 각 응시자들 (P)끼리 맨하탄 거리 2 초과가 되어야 함
    # 단, 응시자끼리 파티션(X)으로 막힌 경우에는 가능
    answer = []
    maps_ = []

    for place in places:
        map_ = []
        for row in place:
            one_row = []
            for c in row:
                one_row.append(c)

            map_.append(one_row)
        maps_.append(map_)

    for map_ in maps_:
        is_distancing = True
        for i in range(5):
            for j in range(5):
                if map_[j][i] == 'P':
                    if not check_other(map_, j, i):
                        is_distancing = False
                elif map_[j][i] == 'O':
                    if not check_block(map_, j, i):
                        is_distancing = False
        if is_distancing:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))