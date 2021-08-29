# 그래디 - 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스(N)에 해당하는 수가 연속으로 K번 초과하여 더해질 수 없는 것이 특징

# input example
## 5 8 3
## 2 4 5 4 6
## -> sort : 2 4 4 5 6
## max_ = 6, second = 5
## 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46

n, m, k = map(int, input().split())
number = list(map(int, input().split()))

number.sort()
max_ = number[n - 1]
second = number[n - 2]

# 큰 수의 수열은 다음과 같은 공식으로 구할 수 있음.
# m = 8, k = 3, 일때, {6 6 6 5} {6 6 6 5} 이므로, 수열은 m / (k + 1)로 성립하며 * k를 하면
# 큰 수가 더해지는 횟수를 구할 수 있음
count = m // (k + 1) * k
# 큰 수가 나누어지지 않는 경우도 고려
count += m % (k + 1)

answer = count * max_
answer += (m - count) * second

print(answer)

# 시간 복잡도 고려 x
## inputs
# n, m, k = map(int, input().split())
# number = list(map(int, input().split()))
#
# # 원소들 오름차순 정렬
# number.sort()
#
# # 가장 큰 수와 두 번째로 큰 수를 구해, 계속 더하기만 하면 됨
# max_ = number[n-1]
# second = number[n-2]
#
# answer = 0
#
# while True:
#     for i in range(k):
#         # k번 반복하며, max_ 값을 더함
#         if m == 0:
#             break
#         answer += max_
#         m -= 1
#
#     # k번 만큼 max_를 더 한 후, second largest number를 한 번 더해줌
#     if m == 0:
#         break
#     answer += second
#     m -= 1
#
# print(answer)
#
