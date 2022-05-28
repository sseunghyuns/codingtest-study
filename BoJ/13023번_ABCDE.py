# DFS
from collections import defaultdict

N, M = map(int, input().split())

relation = defaultdict(list)
visited = [False] * N
for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

            
def dfs(v, depth):
    global answer
    if depth == 4:
        answer = True
        return
    for i in relation[v]:
        if not visited[i]:
            visited[v] = True
            dfs(i, depth+1)
            visited[v] = False
           
answer = False
for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
    if answer:
        break

if answer:
    print(1)
else:
    print(0)
            