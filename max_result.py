# 여러 수의 덧셈('+'), 뺄셈('-'), 곱셈('x')으로 이루어진 식에 괄호 한 쌍을 올바르게 삽입하여 식을 계산123한 결과가 최대가 되도록 하려 합니다.
import warnings

def solution(expression: str):
    warnings.filterwarnings('ignore')

    answer = []
    expression = expression.replace('x', '*')

    def dfs(exp_: str, start: int, end: int):
        nonlocal answer

        if start == end:
            return True

        try:
            answer.append(eval(exp_))
        except:
            pass

        exp_ = exp_.replace('(', '')
        exp_ = exp_.replace(')', '')
        exp_ = '{}{}{}{}{}'.format(exp_[:start], '(', exp_[start:end], ')', exp_[end:])

        dfs(exp_, start + 1, end)

    for i in range(len(expression), 0, -1):
        dfs(expression, 0, i)

    return max(answer)

print(solution("2-1x5-4x3+2"))