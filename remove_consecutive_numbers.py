# 프로그래머스 코딩테스트 연습 - 연습문제 - 같은 숫자는 싫어

# https://programmers.co.kr/learn/courses/30/lessons/12906
# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.

def solution(arr):
    # 빈 배열에 첫 요소 넣어주고, 그 다음 원소와 같은지 다른지만 비교하면 됨
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i - 1] is not arr[i]:
            answer.append(arr[i])
    
    return answer
