import sys

tc=int(sys.stdin.readline())
lists=[]
for i in range(tc):
    s,e=map(int,sys.stdin.readline().split())
    lists.append((s,e))

lists.sort()

start=lists[0][0]
end=lists[0][1]
sum=0

for i in range(tc):
    if i ==0 :
        continue
    a,b=lists[i][0],lists[i][1]

    if a>end:
        sum+=end-start
        start=a
        end=b
    else:
        if b>end:
            end=b


print(end-start+sum)

