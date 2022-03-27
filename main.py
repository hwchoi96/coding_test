def solution(data):
    answer = []
    # 문서 번호, 인쇄 요청 시간, 페이지 수
    # 페이지 수는 1초에 하나씩 처리

    queue = []
    printer = []
    current_time = 0
    limit_time = 0

    done_list = []
    while len(answer) != len(data):
        # 모든 요청을 다 처리할 때까지
        for docu in data:
            # 대기열 후보들을 다 넣음
            if docu[1] <= current_time:
                if docu not in queue and docu not in done_list:
                    done_list.append(docu)
                    queue.append(docu)
        if printer == []:
            # 프린터가 비어 있다면, 바로 넣기
            if queue:
                printer = queue[0]
                queue.pop(0)
        else:
            # 사용 중이라면, 프린트가 빌때까지 대기
            limit_time += 1

        if printer:
            if limit_time >= printer[2]:
                # 프린트가 다 끝났을 때
                answer.append(printer[0])
                printer = []
                limit_time = 0

                # 후보군 찾기, 페이지 수를 기준으로 sort
                queue = sorted(queue, key=lambda x: x[2])
        current_time += 1

    return answer

print(solution([[1, 0, 5],[2, 2, 2],[3, 3, 1],[4, 4, 1],[5, 10, 2]]	))
print(solution([[1, 0, 3], [2, 1, 3], [3, 3, 2], [4, 9, 1], [5, 10, 2]]	))
print(solution([[1, 2, 10], [2, 5, 8], [3, 6, 9], [4, 20, 6], [5, 25, 5]]))