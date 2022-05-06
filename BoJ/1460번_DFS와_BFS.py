from collections import deque

'''
https://www.acmicpc.net/problem/1260
반례1
3 1 1
2 3
-> 출력 결과가
1
1
이어야 한다.
'''

n, m, v = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

data = {}
for i in graph:
    if i[0] not in data:
        data[i[0]] = [i[1]]
    else:
        data[i[0]].append(i[1])
        
    if i[1] not in data:
        data[i[1]] = [i[0]]
    else:
        data[i[1]].append(i[0])

for key, val  in data.items():
    data[key] = sorted(val) # 정점 번호 오름차순으로 정렬

stack = []
visited = [False]*(n+1)

def dfs(vertex):
    
    visited[vertex] = True
    stack.append(vertex)
    for nb in data[vertex]:
        if not visited[nb]:
            dfs(nb)

if v not in data:
    print(v)
    print(v)
else:
    dfs(v)
    for s in stack:
        print(s, end=' ')


    q = deque()
    visited = [False]*(n+1)

    q.append(v)
    visited[v] = True
    bfs = []
    while q:
        now = q.popleft()
        bfs.append(now)
        for nb in data[now]:
            if not visited[nb]:
                q.append(nb)
                visited[nb] = True
    print()
    for s in bfs:
        print(s, end=' ')