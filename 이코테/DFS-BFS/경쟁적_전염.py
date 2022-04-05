'''
우선순위 큐 사용
s = 0인 경우 처리를 해주지 않아 테스트 케이스에서 걸리는 이슈.
'''

import heapq

n, k = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

q = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
          heapq.heappush(q, (graph[i][j], (i,j)))

s, x, y = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

new_q = []

while q:
    if s == 0:
        break
    virus, now = heapq.heappop(q)
    
    for i in range(4):
        nx, ny = now[0]+dx[i], now[1]+dy[i]
        
        if nx<0 or nx>len(graph)-1 or ny<0 or ny>len(graph[0])-1:
            continue
        
        if graph[nx][ny]!=0:
            continue
        
        graph[nx][ny] = virus
        heapq.heappush(new_q, (virus, (nx, ny)))
        
    if len(q)==0:
        s -= 1
        
        if s==0:
            break
        
        if len(new_q)==0:
            break
        else:
            q = new_q
            new_q = []

print(graph[x-1][y-1])
