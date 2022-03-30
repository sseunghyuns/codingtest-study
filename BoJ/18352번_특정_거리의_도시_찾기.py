from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    

queue = deque()
distance = [-1]*(n+1)
distance[x] = 0
queue.append(x)

while queue:
    now = queue.popleft()
    
    for i in graph[now]:
        if distance[i]==-1:
            distance[i] = distance[now] + 1 
            queue.append(i)
counter=0          
for i in range(1, len(distance)):
    if distance[i]==k:
        counter+=1
        print(i)
if counter==0:
    print(-1)
