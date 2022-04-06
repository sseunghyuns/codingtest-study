'''
bfs 문제
걸린 시간: 30분
'''

from collections import deque

m, n = map(int, input().split())

tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

queue = deque()

for i in range(len(tomato)):
    for j in range(len(tomato[0])):
        if tomato[i][j] == 1:
            queue.append((i,j))

answer = -1
dx = [1,-1,0,0]
dy = [0,0,1,-1]

while queue:
    for _ in range(len(queue)):
        now = queue.popleft()
        
        for i in range(4):
            nx, ny = now[0]+dx[i], now[1]+dy[i]
            
            if nx<0 or nx>len(tomato)-1 or ny<0 or ny>len(tomato[0])-1:
                continue
            
            if tomato[nx][ny]==0:
                tomato[nx][ny] = 1
                queue.append((nx, ny))

    answer+=1 # 날짜 업데이트

for i in range(len(tomato)):
    for j in range(len(tomato[0])):
        if tomato[i][j] == 0:
            answer = -1
            break

print(answer)
