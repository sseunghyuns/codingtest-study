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


'''
2번째 풀이
인접한 곳에 익지 않은 토마토가 있으면, 기존 토마토 숫자에 +1하는 방법.
BFS 수행 후 최종 max 값이 정답이 될 것이다.
'''

M, N = map(int, input().split())

tomatoes = []
for _ in range(N):
    tomatoes.append(list(map(int, input().split())))
    
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j]==1:
            q.append((i,j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        if tomatoes[nx][ny]==0:
            tomatoes[nx][ny] = tomatoes[x][y]+1
            q.append((nx, ny))

answer = 0
flag = False
for i in range(N):
    for j in range(M):
        if tomatoes[i][j]==0:
            flag = True
            break
        else:
            answer = max(answer, tomatoes[i][j])
if flag:
    print(-1)
else:
    print(answer-1)

        

            
            

    