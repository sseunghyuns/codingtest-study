'''
첫 시도: bfs로 접근.
다른 사람들의 코드에 비해 상당히 비효율적
'''

import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = defaultdict(list)

for i in range(1, n+1): # 1~n까지의 정점 존재
    graph[i]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(n+1)
start = list(graph.keys())[0]
visited = [start]
queue = deque([start])
answer = 1

while queue:
    now = queue.popleft()
    for v in graph[now]:
        if v not in visited:
            queue.append(v)
            visited.append(v)
    if len(queue)==0:
        if len(visited) != n:
            for k in graph.keys():
                if k not in visited:
                    visited.append(k)
                    queue.append(k)
                    answer+=1
                    break
print(answer)


'''
dfs를 사용한 방식.
1~N까지의 연결 정보를 담은 graph를 생성 후, 연결되어 있는 경우에 대해 dfs를 수행한다.
'''

import sys
sys.setrecursionlimit(10000) 

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[0 for i in range(N + 1)] for j in range(N + 1)]
visited = [False for _ in range(N + 1)]
answer = 0

for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1
    

def dfs(index):
    visited[index] = True
    for i in range(1, N+1):
        if graph[index][i]==1 and not visited[i]:
            dfs(i)
    
for i in range(1, N+1):
    if not visited[i]:
        answer+=1
        dfs(i)
print(answer)