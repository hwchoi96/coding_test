def solution(s, idx):
    answer = []

    for i in idx:
        if s[i] == '{':
            # 왼괄호의 경우, 오른쪽으로 탐색해 가장 처음으로 0이 되는 지점이 짝
            check = 1
            for index in range(i + 1, len(s)):
                if s[index] == '{':
                    check += 1
                elif s[index] == '}':
                    check -= 1

                if check == 0:
                    answer.append(index)
                    break

        elif s[i] == '}':
            # 오른괄호의 경우, 왼쪽으로 탐색해 가장 처음으로 0이 되는 지점이 짝
            check = -1
            for index in range(i - 1, -1, -1):
                if s[index] == '}':
                    check -= 1
                elif s[index] == '{':
                    check += 1

                if check == 0:
                    answer.append(index)
                    break

    return answer

print(solution("{cpp{java}}{python}", [0, 4, 9, 10, 11, 18]	))
print(solution("ab{}cd{efg{}h}{ij}"	, [3, 6, 11, 3, 14, 11]	))