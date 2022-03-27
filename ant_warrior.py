import copy


def verify_P(a, b):
    ab = a + b
    ba = b + a

    if is_P(ab) or is_P(ba):
        return True
    return False


def is_P(a):
    for i in range(0, len(a) // 2):
        if a[i] != a[-i - 1]:
            return False
    return True


def solution(P):
    ans = []
    # 배열 P가 매개변수로 주어질 때, 배열에 있는 모든 원소를 제거하기 위해 첫 번째 원소를
    # 어느 조각과 연결 해야 하는지 모든 가능한 경우를 찾고, 그 경우에 첫 번째 원소와 연결되는 원소들을
    # return 하도록 solution 함수를 완성해 주세요. 위의 예시의 경우는 ["111","211"]을 return 하면 됩니다.
    # return 할 때는 배열에 주어진 순서대로 return 해주세요.

    first = P[0]

    for i in range(1, len(P)):
        temp_ = copy.deepcopy(P)
        next_ = P[i]

        if verify_P(first, next_):
            # 첫 원소와 특정 원소를 선택했을 때 팰린드롬이 가능한 경우,
            try:
                temp_.remove(first)
                temp_.remove(next_)
            except ValueError as e:
                continue

            # 남은 나머지 원소로도 팰린드롬이 되어 빈 배열이 된다면 특정 원소는 조건에 부합함.
            ttemp_ = copy.deepcopy(temp_)
            for i in range(1, len(temp_)):
                if verify_P(temp_[0], temp_[i]):
                    try:
                        ttemp_.remove(temp_[0])
                        ttemp_.remove(temp_[i])
                    except IndexError as e:
                        continue

                    if not ttemp_:
                        ans.append(next_)
    return ans

print(is_P('1111'))
print(is_P('11211'))
print(is_P('12211'))
print(is_P('111211'))
print(is_P('211111'))

print(solution(["11", "111", "11", "211"]))
print(solution(["21", "123", "111", "11"]))
