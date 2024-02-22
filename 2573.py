import copy
import sys
from collections import deque

y,x=map(int,sys.stdin.readline().split())

board=[]

for _ in range(y):
    board.append(list(map(int,sys.stdin.readline().split())))
a=0
def count(b1):
    visited=[[0]*x for _ in range(y)]

    cnt=0
    for i in range(y):
        for k in range(x):
            if b1[i][k]<1:
                visited[i][k]=1

    q=deque()
    for i in range(y):
        for k in range(x):
            if visited[i][k]<1:
                cnt+=1
                if cnt>2:
                    return 2
                q.append((i,k))
                visited[i][k]=1
                while q:
                    a,b=q.pop()
                    if b+1<x and visited[a][b+1]==0:
                        visited[a][b+1]=1
                        q.append((a,b+1))
                    if b-1>=0 and visited[a][b-1]==0:
                        visited[a][b-1]=1
                        q.append((a,b-1))
                    if a+1<y and visited[a+1][b]==0:
                        visited[a+1][b]=1
                        q.append((a+1,b))
                    if a-1>=0 and visited[a-1][b]==0:
                        visited[a-1][b]=1
                        q.append((a-1,b))
    return cnt
ans=0
while 1:

    cboard=copy.deepcopy(board)
    for i in range(y):
        for k in range(x):
            if board[i][k]>0:
                if k+1<x and board[i][k+1]<1:
                    cboard[i][k]-=1
                if k-1>=0 and board[i][k-1]<1:
                    cboard[i][k]-=1
                if i+1<y and board[i+1][k]<1:
                    cboard[i][k]-=1
                if i-1>=0 and board[i-1][k]<1:
                    cboard[i][k]-=1
    counter=0
    for i in range(y):
        for k in range(x):
            if cboard[i][k]>0:
                counter+=1
    if counter==0 or counter==1:
        ans=0
        break
    # for i in range(y):
    #     print(cboard[i])
    a=count(cboard)
    ans+=1
    board=cboard
    if a>1:
        break

print(ans)