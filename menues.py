def solution(orders):
    answer = []

    users = {}

    for order in orders:
        menues = order.split(' ')

        user = menues[0]
        menues = menues[1:]
        menues = list(set(menues))

        if user not in users:
            users[user] = []
            users[user].extend(menues)
        else:
            for menu in menues:
                if menu not in users[user]:
                    users[user].append(menu)

    # max_user = max(users, key=lambda x:x[1])

    max_ = 0
    for v in users.values():
        if len(v) > max_:
            max_ = len(v)
    for k, v in users.items():
        if len(v) == max_:
            answer.append(k)

    # for k, v in users.items():
    #     if len(v) == len(users[max_user]):
    #         answer.append(k)

    return sorted(answer)

print(solution(["alex pizza pasta", "alex pizza pizza", "alex noodle", "bob pasta", "bob noodle sandwich pasta", "bob steak noodle"]	))
print(solution(["alex pizza pasta steak", "bob noodle sandwich pasta", "choi pizza sandwich pizza", "alex pizza pasta steak"]	))
