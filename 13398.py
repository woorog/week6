n = int(input())  # 수열의 길이
arr = list(map(int, input().split()))  # 수열

# 동적 프로그래밍 배열 초기화
dp1 = [0] * n
dp2 = [0] * n

dp1[0] = arr[0]
dp2[0] = arr[0]

# 최대합 계산
for i in range(1, n):
    dp1[i] = max(dp1[i-1] + arr[i], arr[i])
    dp2[i] = max(dp2[i-1] + arr[i], dp1[i-1])

# 수를 제거하지 않은 상태와 제거한 상태에서의 최대합 중 최댓값
answer = max(max(dp1), max(dp2))

print(answer)

# arr:  10,  -4,  3,  1,  5,  6, -35, 12, 21, -1
# dp1:  10,   6,  9
# dp2:  10,  10, 13