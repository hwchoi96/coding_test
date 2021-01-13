# 프로그래머스 코딩테스트 연습 - 연습문제 - 괄호 검사

# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# ()() 또는 (())() 는 올바른 괄호입니다.
# )()( 또는 (()( 는 올바르지 않은 괄호입니다.

# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = False
    
    init = 0
    
    for c in s:
        if init <= -1:
            return answer
        
        if c == '(':
            init += 1
        elif c == ')':
            init -= 1
        else:
            print('Unknown Keyword')
            return answer

    print("실행 결과 : ", init)
    
    if init == 0:
        answer = True
    
    return answer
