from collections import deque
import copy

N = int(input())
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)
indegree = [0] * (N+1)

for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i) # graph[1].append(2) 2번을 듣기 위해선 1번이 우선 수강되어야 함.
        indegree[i] += 1
        
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
                
            result[i] = max(time[i]+result[now], result[i]) # 최소 시간 업데이트
            
    for r in result[1:]:
        print(r)

topology_sort()    