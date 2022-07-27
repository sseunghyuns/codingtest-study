from collections import deque
from copy import deepcopy

N = int(input())

indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)

for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i]+=1
        graph[j].append(i) # graph[1].append(2) 2번을 듣기 위해선 1번이 우선 수강되어야 함.

print(indegree)
print(graph)

def topology_sort():
    result = deepcopy(time)
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i]==0:
            q.append(i)
            
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[now] + time[i], result[i])
            indegree[i]-=1
            
            if indegree[i]==0:
                q.append(i)
                
    for i in range(1, N+1):
        print(result[i])
topology_sort()