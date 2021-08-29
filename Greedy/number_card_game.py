# 숫자 카드 게임
## 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 것
## 1. N x M 형태로 놓인 카드들에서, 뽑고자 하는 카드가 포함되어 있는 행을 선택
## 2. 그 선택된 행에 포함된 카드 중에서 가장 낮은 카드를 뽑음
## 3. 선택된 가장 낮은 카드에서 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 선택

n, m = map(int, input().split())
cards = []

answer = 0

for i in range(n):
    # 입력 받는 동시에 가장 작은 값을 뽑아냄
    card = list(map(int, input().split()))
    min_ = min(card)

    # 이전 행의 가장 작은 값과 현재 행의 가장 작은 값 비교
    answer = max(answer, min_)

print(answer)