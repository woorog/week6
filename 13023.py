import sys

node, tc = map(int, input().split())
dic = {i: [] for i in range(node)}

for _ in range(tc):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

def dfs(now, depth, visited):
    if depth == 4:
        return True
    visited[now] = True
    for next_node in dic[now]:
        if not visited[next_node]:
            if dfs(next_node, depth + 1, visited)==True:
                return True
    visited[now] = False
    return False

result = False
for i in range(node):
    visited = [False] * node
    if dfs(i, 0, visited):
        result = True
        break

print(1 if result else 0)
