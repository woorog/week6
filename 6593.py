import sys
from collections import deque

while 1:

    floor,y,x=map(int,sys.stdin.readline().split())
    if floor==0 and y==0 and x==0:
        break

    board=[]
    for _ in range(floor):
        k=[]
        for i in range(y+1):
            a=list(sys.stdin.readline().strip())
            if a==[]:
                continue
            k.append(a)
        board.append(k)
    start=[]
    end=[]
    for i in range(floor):
        for l in range(y):
            for k in range(x):
                if board[i][l][k]=='S':
                    start.append(i)
                    start.append(l)
                    start.append(k)
                if board[i][l][k]=='E':
                    end.append(i)
                    end.append(l)
                    end.append(k)

    move=0
    q=deque()
    q.append((start[0],start[1],start[2],move))
    min=999999999999
    while q:

        flr,ny,nx,mov=q.popleft()
        if flr==end[0] and ny==end[1] and nx==end[2]:
            if mov<min:
                min=mov
                break

        if flr-1>=0 and board[flr-1][ny][nx]!='#':
            q.append((flr-1,ny,nx,mov+1))
            board[flr-1][ny][nx]='#'
        if flr+1<floor and board[flr+1][ny][nx] !='#' :
            q.append((flr+1,ny,nx,mov+1))
            board[flr+1][ny][nx]='#'
        if ny-1>=0 and board[flr][ny-1][nx]!='#':
            q.append((flr,ny-1,nx,mov+1))
            board[flr][ny-1][nx]='#'
        if ny+1<y and board[flr][ny+1][nx]!='#':
            q.append((flr,ny+1,nx,mov+1))
            board[flr][ny+1][nx]='#'
        if nx-1>=0 and board[flr][ny][nx-1]!='#':
            q.append((flr,ny,nx-1,mov+1))
            board[flr][ny][nx-1]='#'
        if nx+1<x and board[flr][ny][nx+1]!='#':
            q.append((flr,ny,nx+1,mov+1))
            board[flr][ny][nx+1]='#'

    if min ==999999999999:
        print("Trapped!")
    else:
        print(f"Escaped in {min} minute(s)")



from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def building(x, y, z):
    q.append([x, y, z])
    d[x][y][z] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if a[nx][ny][nz] == 'E':
                    print("Escaped in {0} minute(s).".format(d[x][y][z]))
                    return
                if a[nx][ny][nz] == '.' and d[nx][ny][nz] == 0:
                    d[nx][ny][nz] = d[x][y][z] + 1
                    q.append([nx, ny, nz])
    print("Trapped!")

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    a = [[[]*c for _ in range(r)] for _ in range(l)]
    d = [[[0]*c for _ in range(r)] for _ in range(l)]
    q = deque()
    for i in range(l):
        a[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if a[i][j][k] == 'S':
                    building(i, j, k)



