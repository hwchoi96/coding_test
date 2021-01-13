# 프로그래머스 코딩테스트 연습 - 정렬 - H-Index

# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.

# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    
    # H-Index 쉽게 이해 하기
    # - 피인용 횟수를 내림차순 정렬
    # - 각 피인용 횟수와 단계별 논문 갯수(1, 2, 3, 4 ...) 비교
    # - 단계별 피인용 횟수가 논문 갯수보다 많거나 같을때 마다 H-index 하나씩 증가
    
    # [0, 1, 1], 1 이면 = 정렬 후 [1, 1, 0]
    # 단계 : 피인용 - 1, 논문 수 - 1 => H-index ++
    # 단계 : 피인용 - 1, 논문 수 - 2 => 변화 x
    # 단계 : 피인용 - 0, 논문 수 - 3 => 변화 x
    # 해당 H-Index = 1
    
    citations = sorted(citations, reverse=True)
    # 피인용 횟수 내림차순 정렬
    
    for i in range(1, len(citations) + 1):
        if citations[i - 1] >= i:
            # 논문 수는 1에서 시작하고, 배열의 index는 0에서 부터 시작
            answer += 1
        
    return answer
