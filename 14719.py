import sys

y,x=map(int,sys.stdin.readline().split())
blocks=list(map(int,sys.stdin.readline().split()))

ans=0
for i in range(1,x-1):
    bigleft=max(blocks[:i])
    bigright=max(blocks[i:])

    if blocks[i]<bigright and blocks[i]<bigleft:
        lrmin=min(bigleft,bigright)
        ans+=lrmin-blocks[i]

print(ans)