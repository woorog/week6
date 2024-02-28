import sys

n=int(sys.stdin.readline())

lists=list(map(int,sys.stdin.readline().split()))

# 가장 작은 수
m1 = min(lists)

# 인접한 두 면의 합의 최소값 찾기
m2 = min([sum(pair) for pair in [(lists[i], lists[j]) for i in range(6) for j in range(i+1, 6) if not ((i == j) or (i+j == 5))]])

# 세 면이 만나는 경우의 합의 최소값 찾기
m3 = min(lists[0]+lists[1]+lists[2], lists[0]+lists[2]+lists[4],
         lists[0]+lists[4]+lists[3], lists[0]+lists[1]+lists[3],
         lists[5]+lists[1]+lists[2], lists[5]+lists[2]+lists[4],
         lists[5]+lists[4]+lists[3], lists[5]+lists[1]+lists[3])

# 정육면체를 구성할 때의 계산
if n == 1:
    ans = sum(lists) - max(lists)
else:
    ans = m3 * 4 + (4 * (n - 1) + (n - 2) * 4) * m2 + ((n - 2) * (n - 1) * 4 + (n - 2) ** 2) * m1
print(ans)

