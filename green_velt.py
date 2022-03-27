from itertools import combinations

def get_score_same_number(cards):
    rules = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    score = 0

    for cards in cards:
        for rule in rules:
            if cards[1] == rule:
                rules[rule] += 1
                break

    for rule in rules.values():
        # 3개가 넘었으면 모든 경우의 수를 구함.
        if rule >= 3:
            dummy = [i for i in range(rule)]

            for i in range(3, len(dummy) + 1):
                com = list(combinations(dummy, i))
                for c in com:
                    score += (len(c) ** 2)

    return score


def get_score_same_shape(cards):
    rules = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
    score = 0

    for card in cards:
        if card[0] == 'S':
            rules['S'] += 1
        elif card[0] == 'D':
            rules['D'] += 1
        elif card[0] == 'H':
            rules['H'] += 1
        else:
            rules['C'] += 1

    for rule in rules.values():
        if rule >= 3:
            dummy = [i for i in range(rule)]

            for i in range(3, len(dummy) + 1):
                com = list(combinations(dummy, i))
                for c in com:
                    score += (len(c) ** 2)

    return score

def get_score_not_dup(cards):
    # 번호도 카드도 겹치지 않는 카드의 개수 세기
    num_not_dup = []
    alpha_not_dup = []
    score = 0

    for card in cards:
        if card[0] not in alpha_not_dup:
            alpha_not_dup.append(card[0])
        if card[1] not in num_not_dup:
            num_not_dup.append(card[1])

    if len(alpha_not_dup) >= 3 and len(alpha_not_dup) == len(num_not_dup):
        dummy = [i for i in range(len(alpha_not_dup))]

        for i in range(3, len(dummy) + 1):
            com = list(combinations(dummy, i))
            for c in com:
                score += (len(c) ** 2)

    return score

def solution(cards):
    answer = 0

    answer += get_score_same_shape(cards)
    answer += get_score_same_number(cards)
    answer += get_score_not_dup(cards)

    return answer

print(solution(["S1","D3","S3","S4","H3","H1"]))
print(solution(["C8","H8","C7","C0","D8","S8"]))