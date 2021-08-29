# 1이 될때까지
## N이 1이 될때까지 두 개의 연산을 이용할 수 있다. 최소 연산 횟수를 구하라
## 1. N에서 1을 뺀다. 2. N을 K로 나눈다
## 단, 2.는 N이 K로 나누어질 때만 가능

n, k = map(int, input().split())

answer = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n = n // k
        answer += 1
    else:
        n -= 1
        answer += 1

print(answer)