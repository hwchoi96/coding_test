def solution(schedule):
    # 한 수업은 3시간 동안 진행됨
    # 겹치는 케이스를 모두 제거하고 선택할 수 있는 모든 경우의 수 뽑기
    answer = -1

    day_ = {'MO' : 1,
             'TU' : 2,
             'WE' : 3,
             'TH' : 4,
             'FR' : 5}

    table = []

    for subject in schedule:
        for t in subject:
            day = day_[t.split(' ')[0]]
            time = t.split(' ')[1]

            # 수업은 3시간 연속으로 진행됨
            times = time.split(':')[0] + time.split(':')[1]
            candidate = [day, int(times)]
            if not table:
                table.append([day, int(times)])

            is_dup = False
            for i in table:
                if i[0] == candidate[0]:
                    # 요일이 같은 경우, 시간을 조회
                    if abs(i[1] - candidate[1]) <= 300:
                        is_dup = True

            if not is_dup:
                table.append([day, int(times)])
                print(table)

    return answer

print(solution([["MO 12:00", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))