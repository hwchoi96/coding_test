# 프로그래머스 코딩테스트 연습 - 연습문제 - 이상한 문자 만들기

# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    s = s.lower()
    answer = ''
    index = 0
    
    string = s.split(' ')
    
    for s in string:
    
        for c in s:
            if index % 2 == 0:
                answer += c.upper()
            else:
                answer += c
            index += 1
        
        index = 0
        answer += ' '
    answer = answer[:-1]
    
    return answer
