# 프로그래머스 코딩테스트 연습 - 정렬 - 가장 큰 수

# https://programmers.co.kr/learn/courses/30/lessons/42746
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

class Number:
    def __init__(self, str_number, original_digits):
        self.str_number = str_number
        self.original_digits = original_digits
    
    # !! 파이썬에서 sorted를 이용하여 클래스를 정렬하고 싶을 때,
    # __lt__ 메소드 안에 특정 멤버 변수 비교 구문을 적음
    # -> C++의 Operator Overloading과 매우 흡사한 개념
    def __lt__(self, other):
        return self.str_number < other.str_number

def solution(numbers):
    # 파이썬 문자열 < > 부등호 규칙
    # 문자열이 숫자만으로 이루어져 있는 경우, 각 자리수 별로 비교하여
    # 한 자리수가 더 크다면 다음 원소를 확인하지 않고 바로 비교를 끝냄
    ## Important example. "334555" < "337" = Result : True

    answer = ''
    numbers_classes = []
    
    # !!!! 주어진 숫자 그대로 비교하면 테스트 케이스의 3, 30 같은 경우, 30이 크기 때문에 303이 되는
    # 예외 상황이 발생함. 이를 방지하기 위해, 임의의 횟수만큼 숫자를 늘림
    for n in numbers:
        str_number = str(n) * 3
        # Ex. 3 -> 333, 12 -> 121212
        original_digits = len(str(n))
        
        # 늘어난 임의의 문자와 원래 자릿수를 기록
        numbers_classes.append(Number(str_number, original_digits))
    
    sorted_number = sorted(numbers_classes, reverse=True)
    # __lf__에 의해 늘어난 문자끼리 비교함
    
    for i in sorted_number:
        original_number = i.str_number.replace(i.str_number[:i.original_digits], '', 2)
        # 늘어난 문자를 원래의 숫자로 돌리기 위해 str.replace(늘어난 문자[~원래 자릿수])를 2번 수행하면
        # 원래 숫자를 획득할 수 있음.
        # Ex. 1234 -> str() * 3 수행 = 123412341234
        #     123412341234 -> str.replace() 2번 실행 = 1234
        #     즉, replace는 str() * 3의 반대인 str() / 3의 의미
    
        answer += original_number
    
    # 맨 앞의 원소가 0이라는 의미는 가장 큰 수가 0으로, numbers가 다 0이였을 경우임.
    if answer[0] == '0':
        return '0'
    
    return answer
