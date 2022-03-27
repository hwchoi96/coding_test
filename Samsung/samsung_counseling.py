'''
    퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
    상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
'''

FILE_PATH = './samsung_input/samsung_counseling_input.txt'

answer = []


def dfs(schedule, day, reward, limit):
    if day >= limit:
        answer.append(reward)
        return True

    if day + schedule[day][0] <= n:
        # 다음 스케줄을 선택했을 때,
        dfs(schedule, day + schedule[day][0], reward + schedule[day][1], limit)
    # 다음 스케줄을 선택하지 않았을 때,
    dfs(schedule, day + 1, reward, limit)


with open(FILE_PATH, 'r') as f:
    n_tests = int(f.readline().strip())
    # n_tests = int(input().strip())

    for test in range(n_tests):
        n = int(f.readline().strip())
        # n = int(input().strip())

        day = []

        for i in range(n):
            con_day, reward = f.readline().strip().split(' ')
            # con_day, reward = list(input().split(' '))

            day.append([int(con_day), int(reward)])

        dfs(day, 0, 0, n)

        print(max(answer))

        answer = []

