# 부품 확인
# 부품이 N에 있는 매장에서 손님이 요청한 M개 종류의 부품에 대한 확인 여부를 알려주는 프로그램
# 1 <= N <= 1000000
# 1 <= M <= 1000000
# 각 부품이 존재하면 yes, 없으면 no를 출력

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        p = (left + right) // 2

        if arr[p] == target:
            return True
        elif arr[p] > target:
            right = p - 1
        else:
            left = p + 1

    return False

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

def solution(n, arr, m, x):
    arr = sorted(arr)

    for i in x:
        if binary_search(arr, i):
            print('yes', end=' ')
        else:
            print('no', end=' ')

solution(n, arr, m, x)
