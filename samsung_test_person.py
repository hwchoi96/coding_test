# 총 N개의 시험장이 있고, 각각의 시험장마다 응시자들이 있다. i번 시험장에 있는 응시자의 수는 Ai명이다.
# 감독관은 총감독관과 부감독관으로 두 종류가 있다. 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이고,
# 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명이다.
# 각각의 시험장에 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 된다.
# 각 시험장마다 응시생들을 모두 감시해야 한다. 이때, 필요한 감독관 수의 최솟값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 시험장의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 각 시험장에 있는 응시자의 수 Ai (1 ≤ Ai ≤ 1,000,000)가 주어진다.
# 셋째 줄에는 B와 C가 주어진다. (1 ≤ B, C ≤ 1,000,000)

import math

FILE_PATH = './samsung_input/samsung_test_person.txt'

with open(FILE_PATH, 'r') as f:
    n_tests = int(f.readline())

    for test in range(n_tests):
        answer = 0

        num = int(f.readline().strip())

        spots = f.readline().strip().split(' ')
        temp = f.readline().strip().split(' ')
        main_, sub_ = int(temp[0]), int(temp[1])

        for spot in spots:
            spot = int(spot) - main_
            answer += 1

            if spot <= 0:
                continue

            added = math.ceil(spot / sub_)
            answer += added

        print(answer)