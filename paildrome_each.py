import re

def get_palindrome(c):
    if c == c[::-1]:
        return len(c)
    else:
        return -1

def solution(s):
    answer = []

    special_re = '[0-9a-z]'
    number_re = '[^0-9]'
    str_re = '[^a-z]'

    for c in s:
        c = c.lower()

        spe_c = re.sub(special_re, '', c)
        number_c = re.sub(number_re, '', c)
        str_c = re.sub(str_re, '', c)

        spe_p = get_palindrome(spe_c)
        number_p = get_palindrome(number_c)
        str_p = get_palindrome(str_c)

        if spe_p == -1 or number_p == -1 or str_p == -1:
            continue
        else:
            answer.append(spe_p + number_p + str_p)

    if answer == []:
        return 0
    else:
        return max(answer)

print(solution(["!@ab12cCbA21@!!!!!", "!@ab12cCbA21@!", "ab12cCbA21"]	))
print(solution(["data", "science"]	))
print(solution(["a", "0&1*0"]	))