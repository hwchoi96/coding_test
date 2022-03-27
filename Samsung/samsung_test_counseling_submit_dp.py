'''
    퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.
    상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
'''

# DP 버전, N일 까지만 진행하고 더 이상 상담을 못 하기 때문에 DP 버전은 맨 뒤부터 시작해야함.

n = int(input().strip())

day = []
rewards = []
answer = [0] * (n + 1)

for i in range(n):
    con_day, reward = map(int, input().split(' '))

    day.append(con_day)
    rewards.append(reward)

for i in range(n - 1, -1, -1):
    if day[i] + i > n:
        answer[i] = answer[i + 1]
    else:
        answer[i] = max(rewards[i] + answer[i + day[i]], answer[i + 1])
print(answer[0])