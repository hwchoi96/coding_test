# 프로그래머스 코딩테스트 연습 - 해시 - 완주하지 못한 선수

# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    co_participant = collections.Counter(participant)
    co_completion = collections.Counter(completion)
    # collections = 단어의 빈도수를 value 값으로 하는 파이썬 해쉬
    
    answer = co_participant - co_completion
    # 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였기 때문,
    # 전체 참가자 - 완료자 = 통과 못 한 1인
    
    answer = list(answer.elements())
    # collection - colletion = colletion이기 때문에
    # ['leo' : 0]의 형태로 남아 있어 ['leo']로 빼는 과정

    return answer[0] # 'leo'
