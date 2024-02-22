import sys

tc=int(sys.stdin.readline())

for _ in range(tc):
    a=int(sys.stdin.readline())
    coins=list(map(int,sys.stdin.readline().split()))
    end=int(sys.stdin.readline())

    dp=[0]*(end+2)

    for i in range(a):
        dp[0]=1

        for k in range(end+1):
            if k>=coins[i]:
                dp[k]=dp[k]+dp[k-coins[i]]

    print(dp[end])


