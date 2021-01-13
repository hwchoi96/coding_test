# 프로그래머스 2019 카카오 개발자 겨울 인턴십, 크레인 인형뽑기 게임
# description : 
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0

    stack = []
    # 인형이 담길 스택 배열

    max_row = len(board)
    max_col = len(board[0])
    # 2차원 배열의 행, 열 크기 계산

    for move in moves:
        col = move - 1
        # 각 행 - 1이 실제 2차원 배열 인덱스임

        for i in range(0, max_row):
            if board[i][col] != 0:
                obj_type = board[i][col]
                # 각 단계별 인형 타입 추출
                board[i][col] = 0
                # 인형을 뽑았으니, 해당 칸은 인형이 없음

                stack.append(obj_type)

                for j in range(0, len(stack) - 1):
                    if stack[j] == stack[j + 1]:
                        stack.pop(j)
                        stack.pop(j)
                        # 그 다음 요소도 pop 하면 -1 되므로, j 위치 두 번 삭제

                        answer += 2
                        # !! 사라진 인형의 갯수를 출력하는 것이므로, +2가 되어야 함
                        break
                break

    return answer
