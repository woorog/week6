import copy
import sys
from collections import deque

n,hp,drink=map(int,sys.stdin.readline().split())

board=[]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

print(board)

sx=0
sy=0
for i in range(n):
    for k in range(n):
        if board[i][k]==1:
           sy=i
           sx=k

q=deque()
eat=0
visited=[[0]*n for _ in range(n)]
visited[sy][sx]=1
q.append((sy,sx,eat,hp))
max=0

while q:

    y,x,mint,nowhp=q.popleft()
    if mint>max:
        max=mint

    if nowhp+1>=(abs(sy-y)+abs((sx-x))):
        nowhp-=1
        print(nowhp)
        if y-1>=0 and visited[y-1][x]==0:
            visited[y-1][x]=1
            if board[y-1][x]==2:
                mint+=1
                nowhp+=drink

            q.append((y-1,x,mint,nowhp))
        if y+1<n and visited[y+1][x]==0:
            visited[y+1][x]=1
            if board[y+1][x]==2:
                mint+=1
                nowhp+=drink
            q.append((y+1,x,mint,nowhp))
        if x-1>=0 and visited[y][x-1]==0:
            visited[y][x-1]=1
            if board[y][x-1]==2:
                mint+=1
                nowhp+=drink
            q.append((y,x-1,mint,nowhp))
        if x+1<n and visited[y][x+1]==0:
            visited[y][x+1]=1
            if board[y][x+1]==2:
                mint+=1
                nowhp+=drink
            q.append((y,x+1,mint,nowhp))


print(max)