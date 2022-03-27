def solution(skills, boss):
    skill_combo = 0
    skill_count = 0

    # 최대한 많은 수의 스킬을 쓰게 하려면, 가장 약한 스킬부터 딱 한 번씩 쓰게 하면 됨
    skills = sorted(skills, key=lambda x: x[0])

    for skill in skills:
        if skill[1] >= 1:
            boss -= skill[0]
            skill[1] -= 1
            skill_combo += 1
            skill_count += 1

    # 이제 가장 쌘 스킬부터 써서 탐욕법 수행
    skills = sorted(skills, key=lambda x: x[0], reverse=True)

    for skill in skills:
        if boss <= 0:
            break

        if skill[1] != 0:
            while True:
                if skill[1] == 0 or boss <= 0:
                    break

                boss -= skill[0]
                skill[1] -= 1
                skill_count += 1

    if boss > 0:
        return [-1]
    else:
        return [skill_combo, skill_count]

print(solution([[50, 3], [100, 4], [200, 2], [600, 1]], 1024))
print(solution([[100, 3], [70, 2], [200, 5]], 1000000	))
print(solution([[250, 100]], 1001))