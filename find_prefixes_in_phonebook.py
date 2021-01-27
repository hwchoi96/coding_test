# 프로그래머스 코딩테스트 연습 - 해시 - 전화번호 목록

# https://programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다. 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

def solution(phone_book):
    phone_book = sorted(phone_book)
    # 접두사 판단시 반복문 횟수를 줄이기 위해 가장 작은 자릿수 문자열부터 정렬
    
    for i in range(0, len(phone_book)): # 접두사 추출
        for j in range(i, len(phone_book) - 1):# 접두사 유무 판별
            if phone_book[i] in phone_book[j + 1]:
                # 특정 전화번호에 접두사 후보가 존재할 시,
                
                compare = phone_book[j + 1]
                end_length = len(phone_book[i])
            
                if phone_book[i] == compare[:end_length]:            
                    return False
                # 해당 후보가 "전화번호의 맨 앞에 있는지" 확인하고, 접두사라면 False

    return True
