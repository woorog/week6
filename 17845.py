import sys

tc,cost=map(int,sys.stdin.readline().split())

dp = [0] * (cost + 1)

# 각 단원을 순회하며 dp 테이블 업데이트
for i in range(tc):

    time, S = map(int, sys.stdin.readline().split())  # 각 단원의 예상 공부 시간과 배점
    # 뒤에서부터 현재 단원의 예상 공부 시간만큼 뺀 위치까지 순회
    for j in range(cost, time - 1, -1):
        # 현재 위치의 점수와 현재 위치에서 예상 공부 시간을 뺀 위치의 점수 + 현재 단원의 점수 중 더 큰 값을 선택
        dp[j] = max(dp[j], dp[j - time] + S)


# 최대 점수 출력
print(dp[cost])