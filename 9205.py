import sys
from collections import deque


tc=int(sys.stdin.readline())

for _ in range(tc):

    martlist=[]
    mart=int(sys.stdin.readline())
    x,y=map(int,sys.stdin.readline().split())

    for i in range(mart):
        S,E=map(int,sys.stdin.readline().split())
        martlist.append((S,E))
    Ex,Ey=map(int,sys.stdin.readline().split())
    ans=0
    q=deque()
    q.append((x,y))

    while q:
        x,y=q.pop()
        if abs(Ex-x)+abs(Ey-y)<=1000:
            ans=1
            break
        for i,l in martlist:
            if abs(i-x)+abs(l-y) <= 1000:
                q.append((i,l))
                martlist.remove((i,l))
    if ans==1:
        print("happy")
    else:
        print("sad")


