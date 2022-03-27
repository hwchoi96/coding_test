# 떡볶이 떡 만들기
# 절단기에 높이 h를 지정하면 줄지어진 떡이 한 번에 절단한다. 높이가 h보다 긴 떡은 h 위의 부분이 잘리고, 낮은 떡은 잘리지 않는다.
# 손님이 왔을 때 요청한 총 길이가 m일 때 적어도 m 만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값을 구하는 프로그램을 작성하시오

# 떡 개수 n과 요청한 떡 길이 m: 1 <= n <= 1000000, 1 <= m <= 2000000000
# 둘째 줄에는 개별 떡의 길이이며 높이는 0 <= h <= 1000000000 이다.

n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split()))

# 10억까지 가능이므로, 연산량을 위해서 이진 탐색을 수행해야 함
# 떡을 특정 값으로 잘랐을 때, 전체 조건에 부합하는 곳을 찾으면 됨
# 이를 이진 탐색을 이용한 파라메트릭 서치라고 함
def solution(n, m, arr):
    answer = 0
    left = 0
    right = max(arr)

    while left <= right:
        p = (left + right) // 2
        total = 0

        for i in arr:
            if i > p:
                total += (i - p)

        if total < m:
            right = p - 1
        else:
            answer = p
            left = p + 1

    return answer

print(solution(n, m, arr))