# 프로그래머스 - 코딩테스트 연습 - 완전탐색 - 모의고사

# https://programmers.co.kr/learn/courses/30/lessons/42840
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    answer = []
    
    math_disliker_1_pattern = [1, 2, 3, 4, 5] # element count = 5
    math_disliker_2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]  # element count = 8
    math_disliker_3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # element count = 10
    
    score_1 = 0
    score_2 = 0
    score_3 = 0 # 각 수포자 정답 횟수
    
    for i in range(0, len(answers)):
        if answers[i] == math_disliker_1_pattern[i % 5]:
            score_1 += 1
            
        if answers[i] == math_disliker_2_pattern[i % 8]:
            score_2 += 1
            
        if answers[i] == math_disliker_3_pattern[i % 10]:
            score_3 += 1
    # 정답 비교
    
    # 최득점자 추출을 위한 임시 배열
    scores = [score_1, score_2, score_3]
    
    # 최득점자 추출, 최득점자가 여러 명이라면 여러 명 모두 들어감.
    # 한 명도 맞추지 못했다면 0이 들어감.
    for disliker, score in enumerate(scores):
        if score == max(scores):
            answer.append(disliker + 1)
    
    return answer
