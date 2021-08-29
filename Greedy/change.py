# 그래디 - 거스름돈
# 손님에게 거슬러 주어야 할 돈이 N원일 때, 거슬러 줘야할 동전의 최소 개수를 구하라.

n = 1260
change = [500, 100, 50, 10]

count = 0

for c in change:
    count += (n // c)
    n = n % c

print(count)